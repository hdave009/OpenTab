import psycopg2

# open_db_connection() opens up a connection to the PostgreSQL database.


def open_db_connection():
    # Connect to database
    con = psycopg2.connect(
        host="*********",
        database="*********",
        user="*********",
        password="**********",
        port=5432)
    con.autocommit = True

    return con

# close_db_connection(con) closes a connection to the PostgreSQL database.


def close_db_connection(con):
    # Close connection
    con.close()

# get_course_urls(course) returns a list of all urls associated with a given course


def get_course_urls(course):
    con = open_db_connection()
    cur = con.cursor()
    query = f"SELECT urls FROM courses WHERE course = '{course}'"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    close_db_connection(con)
    urls = []
    for url in rows:
        print(url)
        urls.append(url[0])
    return urls

# add_course_urls(course, urls) adds urls associated with course to SQL database.


def get_courses():
    con = open_db_connection()
    cur = con.cursor()
    query = "SELECT course FROM courses"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    close_db_connection(con)
    urls = []
    for url in rows:
        urls.append(url[0])
    return set(urls)


def url_format(url):
    if(not (url[:7] == 'http://' or url[:8] == 'https://')):
        url = 'http://' + url
    return url


def add_course_urls(course, urls):
    con = open_db_connection()
    cur = con.cursor()
    for url in urls:
        query = "INSERT INTO courses (course, urls) VALUES (%s,%s);"
        cur.execute(query, (course, url_format(url)))
    cur.close()
    close_db_connection(con)


def del_url(course, url):
    con = open_db_connection()
    cur = con.cursor()
    if(url == None):
        cur.execute("DELETE FROM courses WHERE course = %s", (course,))
    else:
        cur.execute(
            "DELETE FROM courses WHERE course = %s AND urls = %s", (course, url))
    cur.close()
    close_db_connection(con)


def main():
    # del_url('CS136')
    # get_course_urls('CS136')
    pass


if __name__ == "__main__":
    main()

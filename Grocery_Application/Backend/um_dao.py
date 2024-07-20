
def get_ums(collection):
    cursor = collection.cursor()
    query = ("SELECT * from um")
    cursor.execute(query)

    response = []
    for (um_id, um_name) in cursor:
        response.append({
            "um_id": um_id,
            "um_name": um_name
        })

    return response

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_ums(connection))
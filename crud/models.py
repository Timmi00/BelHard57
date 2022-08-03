import psycopg2


class CRUDCategory:

    @staticmethod
    def create_session(func):
        def wrapper(**kwargs):
            conn = psycopg2.connect("postgresql://tim:qwerty@localhost:5432/bh57")
            cur = conn.cursor()
            return func(**kwargs, cur=cur, conn=conn)
        return wrapper()

    @staticmethod
    @create_session
    def add(name: str, cur=None, conn=None) -> None:
        cur.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name, ))
        conn.commit()

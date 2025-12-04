from db.connection import cursor, connection

class Category:
    def __init__(self, name, id=None):
        self.id=id
        self.name=name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or not value.strip():
            raise ValueError("Category name must be a non-empty string.")
        self._name=value.strip()

    @classmethod
    def create(cls,name):
        cursor.execute("INSERT INTO categories(name) VALUES(?)",(name,))
        connection.commit()
        return cls(name, cursor.lastrowid)

    @classmethod
    def get_all(cls):
        rows=cursor.execute("SELECT * FROM categories").fetchall()
        return [cls(r["name"], r["id"]) for r in rows]

    @classmethod
    def find_by_id(cls,id):
        r=cursor.execute("SELECT * FROM categories WHERE id=?",(id,)).fetchone()
        return cls(r["name"], r["id"]) if r else None

    def delete(self):
        cursor.execute("DELETE FROM expenses WHERE category_id=?", (self.id,))
        cursor.execute("DELETE FROM categories WHERE id=?", (self.id,))
        connection.commit()

    def expenses(self):
        from models.expense import Expense
        rows=cursor.execute("SELECT * FROM expenses WHERE category_id=?", (self.id,)).fetchall()
        return [Expense(r["amount"], r["date"], r["category_id"], r["note"], r["id"]) for r in rows]

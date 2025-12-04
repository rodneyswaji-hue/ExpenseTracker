from db.connection import cursor, connection
from models.category import Category

class Expense:
    def __init__(self, amount, date, category_id, note=None, id=None):
        self.id=id
        self.amount=amount
        self.date=date
        self.category_id=category_id
        self.note=note

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,v):
        if not isinstance(v,(int,float)) or v<=0:
            raise ValueError("Amount must be positive.")
        self._amount=v

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,v):
        if not isinstance(v,str) or not v.strip():
            raise ValueError("Invalid date.")
        self._date=v.strip()

    @property
    def category_id(self):
        return self._category_id
    @category_id.setter
    def category_id(self,v):
        if Category.find_by_id(v) is None:
            raise ValueError("Category does not exist.")
        self._category_id=v

    @classmethod
    def create(cls, amount, note, date, category_id):
        cursor.execute(
            "INSERT INTO expenses(amount,note,date,category_id) VALUES(?,?,?,?)",
            (amount,note,date,category_id)
        )
        connection.commit()
        return cls(amount,date,category_id,note,cursor.lastrowid)

    @classmethod
    def get_all(cls):
        rows=cursor.execute("SELECT * FROM expenses").fetchall()
        return [cls(r["amount"], r["date"], r["category_id"], r["note"], r["id"]) for r in rows]

    @classmethod
    def find_by_id(cls,id):
        r=cursor.execute("SELECT * FROM expenses WHERE id=?",(id,)).fetchone()
        return cls(r["amount"], r["date"], r["category_id"], r["note"], r["id"]) if r else None

    def delete(self):
        cursor.execute("DELETE FROM expenses WHERE id=?", (self.id,))
        connection.commit()

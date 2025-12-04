from db.schema import create_tables
from cli.main_menu import main_menu

if __name__=='__main__':
    create_tables()
    main_menu()

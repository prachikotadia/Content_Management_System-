import mysql.connector
from mysql.connector import Error

# Database configuration
db_config = {
    "host": "localhost",
    "user": "prachiky",
    "password": "Dhima@hi0511",
    "database": "cms",
}

# Create database connection
def create_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

def execute_query(conn, query, params=None):
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    return cursor.fetchall() if cursor.with_rows else conn.commit()

def print_colored(text, color_code):
    END = '\033[0m'  # Resets color
    print(f'\033[{color_code}m{text}{END}')
   
def colored_input(prompt, color_code):
    END = '\033[0m'  # Resets color
    return input(f'\033[{color_code}m{prompt}{END}')


def main_menu(conn):
    choice = display_main_menu()
    while True:
        if choice == "1":
            #crud_operations_menu
            choice = display_table_list()
            while True:
                if choice == "1":
                    choice = handle_author_operation()  
                elif choice == "2":
                    choice = handle_blog_operation()
                elif choice == "3":
                    choice = handle_category_operation()
                elif choice == "4":
                    choice = handle_content_operation()
                elif choice == "5":
                    choice = handle_content_category_operation()
                elif choice == "6":
                    choice = handle_content_tag_operation()
                elif choice == "7":
                    choice = handle_role_operation()
                elif choice == "8":
                    choice = handle_tag_operation()
                elif choice == "9":
                    choice = handle_user_blog_operation()
                elif choice == "10":
                    choice = handle_user_content_operation()
                elif choice == "11":
                    choice = handle_user_roles_operation()
                elif choice == "12":
                    choice = handle_user_operation()
                elif choice == "13":
                    choice = display_main_menu()
                    break
                else:
                    print("Invalid choice, please choose again.")
                    choice = display_table_list()
                    break

        elif choice == "2":
        #complex_operations_menu
           choice = handle_advanced_menu()

        elif choice == "3":
            break
        else:
            print("Invalid choice, please choose it again.")
        break

def display_main_menu():
    print_colored("\n=== Content Management System ===", 35)
    print_colored("1. To Modify the Data", 33)
    print_colored("2. Complex SQL Operations", 33)
    print_colored("3. Exit", 33)
    return colored_input("Enter your choice (1-3): ", 36)
    
def display_table_list():
    print_colored("\n=== To Modify the Data by Table ===", 35)
    print("1. Author Table")
    print("2. Blogs Table")
    print("3. Category Table")
    print("4. Content Table")
    print("5. Content Category")
    print("6. Content Tag")
    print("7. Roles Table")
    print("8. Tags Table")
    print("9. User Blogs")
    print("10. User Content")
    print("11. User Roles")
    print("12. User Table")
    print("13. Return to Previous Menu")
    return colored_input("Select a table to modify (1-13): ", 36)
    
def display_advance_operation_menu():
    print_colored("\n=== Complex SQL Operations ===", 35)
    print("1. Combaine tables using UNION")
    print("2. Print common values using INNER JOIN")
    print("3. To specify multiple values using IN")
    print("4. To fulfil subquery condition using ANY")
    print("5. To extract all records using ALL")
    print("6. To test the existence of any record using EXITS")
    print("7. To returns the number of rows using COUNT")
    print("8. OLAP query")
    print("9. Return to Previous Menu")
    return colored_input("Select a table to modify (1-9): ", 36)
    
def display_crud_operation_menu(tablename):
    print_colored("\n=== To Modify the Data ===", 34)
    print("1. Add New " + tablename)
    print("2. Read " + tablename + " Data")
    print("3. Update " + tablename + " Data")
    print("4. Delete " + tablename )
    print("5. Return to Previous Menu")
    return colored_input("Enter your choice (1-5): ", 36)

def handle_user_operation():
    choice = display_crud_operation_menu("User")
    while True:
        if choice == "1":
            # Add New User
            username, email, password, hasedpassword = input("Enter username: "), input("Enter email: "), input("Enter password: "), input("Enter hashedpassword: ")
            query = "INSERT INTO User (Username, Email, Password, HashedPassword) VALUES (%s, %s, %s, %s)"
            execute_query(conn, query, (username, email, password, hasedpassword))
            print_colored("User added successfully.", 32)

        elif choice == "2":
            # Read User Data
            username = input("Enter username to search: ")
            query = "SELECT * FROM User WHERE Username = %s"
            results = execute_query(conn, query, (username,))
            print_colored("User Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update User Data
            user_id, new_username, new_email = input("Enter user ID to update: "), input("Enter new username: "), input("Enter new email: ")
            query = "UPDATE User SET Username = %s, Email = %s WHERE UserID = %s"
            execute_query(conn, query, (new_username, new_email, user_id))
            print_colored("User updated successfully.", 32)

        elif choice == "4":
            # Delete User
            user_id = input("Enter user ID to delete: ")
            query = "DELETE FROM User WHERE UserID = %s"
            execute_query(conn, query, (user_id,))
            print_colored("User deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("User")

def handle_user_blog_operation(conn):
    choice = display_crud_operation_menu("User_Blog")
    while True:
        if choice == "1":
            # Add New User-Blog Association
            user_id, blog_id = input("Enter user ID: "), input("Enter blog ID: ")
            query = "INSERT INTO User_Blogs (UserID, BlogID) VALUES (%s, %s)"
            execute_query(conn, query, (user_id, blog_id))
            print_colored("User-Blog association added successfully.", 32)

        elif choice == "2":
            # Read User-Blog Data
            user_id, blog_id = input("Enter user ID: "), input("Enter blog ID: ")
            query = "SELECT * FROM User_Blogs WHERE UserID = %s AND BlogID = %s"
            results = execute_query(conn, query, (user_id, blog_id))
            print_colored("User-Blog association Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update User-Blog Data
            old_user_id, old_blog_id = input("Enter current user ID: "), input("Enter current blog ID: ")
            new_user_id, new_blog_id = input("Enter new user ID: "), input("Enter new blog ID: ")
            query = "UPDATE User_Blogs SET UserID = %s, BlogID = %s WHERE UserID = %s AND BlogID = %s"
            execute_query(conn, query, (new_user_id, new_blog_id, old_user_id, old_blog_id))
            print_colored("User-Blog association updated successfully.", 32)

        elif choice == "4":
            # Delete User-Blog Association
            user_id, blog_id = input("Enter user ID to delete: "), input("Enter blog ID to delete: ")
            query = "DELETE FROM User_Blogs WHERE UserID = %s AND BlogID = %s"
            execute_query(conn, query, (user_id, blog_id))
            print_colored("User-Blog association deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("User_Blog")

def handle_user_roles_operation():
    choice = display_crud_operation_menu("User_Roles")
    while True:
        if choice == "1":
            # Add New User-Role Association
            user_id, role_id = input("Enter user ID: "), input("Enter role ID: ")
            query = "INSERT INTO User_Roles (UserID, RoleID) VALUES (%s, %s)"
            execute_query(conn, query, (user_id, role_id))
            print_colored("User-Role association added successfully.", 32)

        elif choice == "2":
            # Read User-Role Data
            user_id = input("Enter user ID to search: ")
            query = "SELECT * FROM User_Roles WHERE UserID = %s"
            results = execute_query(conn, query, (user_id,))
            print_colored("User-Role association Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update User-Role Data
            user_id = input("Enter user ID for update: ")
            new_role_id = input("Enter new role ID: ")
            query = "UPDATE User_Roles SET RoleID = %s WHERE UserID = %s"
            execute_query(conn, query, (new_role_id, user_id))
            print_colored("User-Role association updated successfully.", 32)

        elif choice == "4":
            # Delete User-Role Association
            user_id, role_id = input("Enter user ID to delete: "), input("Enter role ID to delete: ")
            query = "DELETE FROM User_Roles WHERE UserID = %s AND RoleID = %s"
            execute_query(conn, query, (user_id, role_id))
            print_colored("User-Role association deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("User_Roles")


def handle_user_content_operation():
    choice = display_crud_operation_menu("User_Content")
    while True:
        if choice == "1":
            # Add New User-Content Association
            user_id, content_id = input("Enter user ID: "), input("Enter content ID: ")
            query = "INSERT INTO User_Content (UserID, ContentID) VALUES (%s, %s)"
            execute_query(conn, query, (user_id, content_id))
            print_colored("User-Content association added successfully.", 32)

        elif choice == "2":
            # Read User-Content Data
            user_id, content_id = input("Enter user ID: "), input("Enter content ID: ")
            query = "SELECT * FROM User_Content WHERE UserID = %s AND ContentID = %s"
            results = execute_query(conn, query, (user_id, content_id))
            print_colored("User-Content association Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update User-Content Data
            old_user_id, old_content_id = input("Enter current user ID: "), input("Enter current content ID: ")
            new_user_id, new_content_id = input("Enter new user ID: "), input("Enter new content ID: ")
            query = "UPDATE User_Content SET UserID = %s, ContentID = %s WHERE UserID = %s AND ContentID = %s"
            execute_query(conn, query, (new_user_id, new_content_id, old_user_id, old_content_id))
            print_colored("User-Content association updated successfully.", 32)

        elif choice == "4":
            # Delete User-Content Association
            user_id, content_id = input("Enter user ID to delete: "), input("Enter content ID to delete: ")
            query = "DELETE FROM User_Content WHERE UserID = %s AND ContentID = %s"
            execute_query(conn, query, (user_id, content_id))
            print_colored("User-Content association deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("User_Content")

def handle_author_operation():
    choice = display_crud_operation_menu("Author")
    while True:
        if choice == "1":
            # Add New Author
            first_name, last_name = input("Enter first name: "), input("Enter last name: ")
            query = "INSERT INTO Author (FirstName, LastName) VALUES (%s, %s)"
            execute_query(conn, query, (first_name, last_name))
            print_colored("Author added successfully.", 32)

        elif choice == "2":
            # Read Author Data
            author_id = input("Enter author ID to search: ")
            query = "SELECT * FROM Author WHERE AuthorID = %s"
            results = execute_query(conn, query, (author_id,))
            print_colored("Author Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Author Data
            author_id, new_first_name, new_last_name = input("Enter author ID to update: "), input("Enter new first name: "), input("Enter new last name: ")
            query = "UPDATE Author SET FirstName = %s, LastName = %s WHERE AuthorID = %s"
            execute_query(conn, query, (new_first_name, new_last_name, author_id))
            print_colored("Author updated successfully.", 32)

        elif choice == "4":
            # Delete Author
            author_id = input("Enter author ID to delete: ")
            query = "DELETE FROM Author WHERE AuthorID = %s"
            execute_query(conn, query, (author_id,))
            print_colored("Author deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("Author")

def handle_content_tag_operation():
    choice = display_crud_operation_menu("Content_Tag")
    while True:
        if choice == "1":
            # Add New Content-Tag Association
            content_id, tag_id = input("Enter content ID: "), input("Enter tag ID: ")
            query = "INSERT INTO Content_Tag (ContentID, TagID) VALUES (%s, %s)"
            execute_query(conn, query, (content_id, tag_id))
            print_colored("Content-Tag association added successfully.", 32)

        elif choice == "2":
            # Read Content-Tag Data
            content_id, tag_id = input("Enter content ID: "), input("Enter tag ID: ")
            query = "SELECT * FROM Content_Tag WHERE ContentID = %s AND TagID = %s"
            results = execute_query(conn, query, (content_id, tag_id))
            print_colored("Content-Tag association Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Content-Tag Data
            old_content_id, old_tag_id = input("Enter current content ID: "), input("Enter current tag ID: ")
            new_content_id, new_tag_id = input("Enter new content ID: "), input("Enter new tag ID: ")
            query = "UPDATE Content_Tag SET ContentID = %s, TagID = %s WHERE ContentID = %s AND TagID = %s"
            execute_query(conn, query, (new_content_id, new_tag_id, old_content_id, old_tag_id))
            print_colored("Content-Tag association updated successfully.", 32)

        elif choice == "4":
            # Delete Content-Tag Association
            content_id, tag_id = input("Enter content ID to delete: "), input("Enter tag ID to delete: ")
            query = "DELETE FROM Content_Tag WHERE ContentID = %s AND TagID = %s"
            execute_query(conn, query, (content_id, tag_id))
            print_colored("Content-Tag association deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("Content_Tag")

def handle_content_category_operation():
    choice = display_crud_operation_menu("Content_Category")
    while True:
        if choice == "1":
            # Add New Content-Category Association
            content_id, category_id = input("Enter content ID: "), input("Enter category ID: ")
            query = "INSERT INTO Content_Category (ContentID, CategoryID) VALUES (%s, %s)"
            execute_query(conn, query, (content_id, category_id))
            print_colored("Content-Category association added successfully.", 32)

        elif choice == "2":
            # Read Content-Category Data
            content_id, category_id = input("Enter content ID: "), input("Enter category ID: ")
            query = "SELECT * FROM Content_Category WHERE ContentID = %s AND CategoryID = %s"
            results = execute_query(conn, query, (content_id, category_id))
            print_colored("Content-Category association Read successfully.", 32)

            for row in results:
                print(row)

        elif choice == "3":
            # Update Content-Category Data
            old_content_id, old_category_id = input("Enter current content ID: "), input("Enter current category ID: ")
            new_content_id, new_category_id = input("Enter new content ID: "), input("Enter new category ID: ")
            query = "UPDATE Content_Category SET ContentID = %s, CategoryID = %s WHERE ContentID = %s AND CategoryID = %s"
            execute_query(conn, query, (new_content_id, new_category_id, old_content_id, old_category_id))
            print_colored("Content-Category association updated successfully.", 32)

        elif choice == "4":
            # Delete Content-Category Association
            content_id, category_id = input("Enter content ID to delete: "), input("Enter category ID to delete: ")
            query = "DELETE FROM Content_Category WHERE ContentID = %s AND CategoryID = %s"
            execute_query(conn, query, (content_id, category_id))
            print_colored("Content-Category association deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("Content_Category")

def handle_blog_operation():
    choice = display_crud_operation_menu("Blogs")
    while True:
        if choice == "1":
            # Add New Blog
            blog_title, blog_content, date_published, author_id = input("Enter blog title: "), input("Enter blog content: "), input("Enter date published (YYYY-MM-DD): "), input("Enter author ID: ")
            query = "INSERT INTO Blogs (BlogTitle, BlogContent, DatePublished, AuthorID) VALUES (%s, %s, %s, %s)"
            execute_query(conn, query, (blog_title, blog_content, date_published, author_id))
            print_colored("Blog added successfully.", 32)

        elif choice == "2":
            # Read Blog Data
            blog_id = input("Enter blog ID to search: ")
            query = "SELECT * FROM Blogs WHERE BlogID = %s"
            results = execute_query(conn, query, (blog_id,))
            print_colored("Blog Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Blog Data
            blog_id, new_blog_title, new_blog_content, new_date_published = input("Enter blog ID to update: "), input("Enter new blog title: "), input("Enter new blog content: "), input("Enter new date published (YYYY-MM-DD): ")
            query = "UPDATE Blogs SET BlogTitle = %s, BlogContent = %s, DatePublished = %s WHERE BlogID = %s"
            execute_query(conn, query, (new_blog_title, new_blog_content, new_date_published, blog_id))
            print_colored("Blog updated successfully.", 32)

        elif choice == "4":
            # Delete Blog
            blog_id = input("Enter blog ID to delete: ")
            query = "DELETE FROM Blogs WHERE BlogID = %s"
            execute_query(conn, query, (blog_id,))
            print_colored("Blog deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("Blogs")

             
def handle_role_operation():
    choice = display_crud_operation_menu("Role")
    while True:
        if choice == "1":
            # Add New Role
            role_name, description = input("Enter role name: "), input("Enter description: ")
            query = "INSERT INTO Roles (RoleName, Description) VALUES (%s, %s)"
            execute_query(conn, query, (role_name, description))
            print_colored("Role added successfully.", 32)
            choice = display_crud_operation_menu("Role")

        elif choice == "2":
            # Read Role Data
            role_id = input("Enter role ID to search: ")
            query = "SELECT * FROM Roles WHERE RoleID = %s"
            results = execute_query(conn, query, (role_id,))
            print_colored("Role Read successfully.", 32)
            for row in results:
                print(row)
            choice = display_crud_operation_menu("Role")

        elif choice == "3":
            # Update Role Data
            role_id, new_role_name, new_description = input("Enter role ID to update: "), input("Enter new role name: "), input("Enter new description: ")
            query = "UPDATE Roles SET RoleName = %s, Description = %s WHERE RoleID = %s"
            execute_query(conn, query, (new_role_name, new_description, role_id))
            print_colored("Role updated successfully.", 32)
            choice = display_crud_operation_menu("Role")

        elif choice == "4":
            # Delete Role
            role_id = input("Enter role ID to delete: ")
            query = "DELETE FROM Roles WHERE RoleID = %s"
            execute_query(conn, query, (role_id,))
            print_colored("Role deleted successfully.", 32)
            choice = display_crud_operation_menu("Role")

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.")
            choice = display_crud_operation_menu("Role")

def handle_tag_operation():
    choice = display_crud_operation_menu("Tag")
    while True:
        if choice == "1":
            # Add New Tag
            tag_name = input("Enter tag name: ")
            query = "INSERT INTO Tags (TagName) VALUES (%s)"
            execute_query(conn, query, (tag_name,))
            print_colored("Tag added successfully.", 32)

        elif choice == "2":
            # Read Tag Data
            tag_id = input("Enter tag ID to search: ")
            query = "SELECT * FROM Tags WHERE TagID = %s"
            results = execute_query(conn, query, (tag_id,))
            print_colored("Tag Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Tag Data
            tag_id, new_tag_name = input("Enter tag ID to update: "), input("Enter new tag name: ")
            query = "UPDATE Tags SET TagName = %s WHERE TagID = %s"
            execute_query(conn, query, (new_tag_name, tag_id))
            print_colored("Tag updated successfully.", 32)

        elif choice == "4":
            # Delete Tag
            tag_id = input("Enter tag ID to delete: ")
            query = "DELETE FROM Tags WHERE TagID = %s"
            execute_query(conn, query, (tag_id,))
            print_colored("Tag deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("Tag")

def handle_content_operation():
    choice = display_crud_operation_menu("Content")
    while True:
        if choice == "1":
            # Add New Content
            title, body, author_id = input("Enter content title: "), input("Enter content body: "), input("Enter author ID: ")
            query = "INSERT INTO Content (Title, Body, AuthorID) VALUES (%s, %s, %s)"
            execute_query(conn, query, (title, body, author_id))
            print_colored("Content added successfully.", 32)

        elif choice == "2":
            # Read Content Data
            content_id = input("Enter content ID to search: ")
            query = "SELECT * FROM Content WHERE ContentID = %s"
            results = execute_query(conn, query, (content_id,))
            print_colored("Content Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Content Data
            content_id, new_title, new_body = input("Enter content ID to update: "), input("Enter new title: "), input("Enter new body: ")
            query = "UPDATE Content SET Title = %s, Body = %s WHERE ContentID = %s"
            execute_query(conn, query, (new_title, new_body, content_id))
            print_colored("Content updated successfully.", 32)

        elif choice == "4":
            # Delete Content
            content_id = input("Enter content ID to delete: ")
            query = "DELETE FROM Content WHERE ContentID = %s"
            execute_query(conn, query, (content_id,))
            print_colored("Content deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("Content")

def handle_category_operation():
    choice = display_crud_operation_menu("Category")
    while True:
        if choice == "1":
            # Add New Category
            category_name, keyword = input("Enter category name: "), input("Enter keyword: ")
            query = "INSERT INTO Category (CategoryName, Keyword) VALUES (%s, %s)"
            execute_query(conn, query, (category_name, keyword))
            print_colored("Category added successfully.", 32)

        elif choice == "2":
            # Read Category Data
            category_id = input("Enter category ID to search: ")
            query = "SELECT * FROM Category WHERE CategoryID = %s"
            results = execute_query(conn, query, (category_id,))
            print_colored("Category Read successfully.", 32)
            for row in results:
                print(row)

        elif choice == "3":
            # Update Category Data
            category_id, new_category_name, new_keyword = input("Enter category ID to update: "), input("Enter new category name: "), input("Enter new keyword: ")
            query = "UPDATE Category SET CategoryName = %s, Keyword = %s WHERE CategoryID = %s"
            execute_query(conn, query, (new_category_name, new_keyword, category_id))
            print_colored("Category updated successfully.", 32)

        elif choice == "4":
            # Delete Category
            category_id = input("Enter category ID to delete: ")
            query = "DELETE FROM Category WHERE CategoryID = %s"
            execute_query(conn, query, (category_id,))
            print_colored("Category deleted successfully.", 32)

        elif choice == "5":
            return display_table_list()
        else:
            print("Invalid choice, please choose again.") 
            choice = display_crud_operation_menu("Category")



def handle_advanced_menu():
    choice = display_advance_operation_menu()
    while True:
        if choice == "1":
            query = ('SELECT Username FROM User UNION SELECT Name_Firstname FROM Author')
            results = execute_query(conn, query)
            print_colored("\nCombined List of Usernames and Author First Names:", 32)
            for row in results:
                print(row) 
            choice = display_advance_operation_menu()

        elif choice == "2":
            query = ('SELECT user.Username FROM User INNER JOIN Author ON User.Username = Author.Name_Firstname')
            results = execute_query(conn, query)
            print_colored("\nCommon names that exist both in User and Author tables:",32)
            for row in results:
                    print(row)
            choice = display_advance_operation_menu()

        elif choice == "3":
            query = ("SELECT * FROM User WHERE UserID IN (SELECT UserID FROM Author);")
            results = execute_query(conn, query)
            print_colored("\nMultiple values of User and Tables:", 32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "4":
            query = ('SELECT * FROM Content WHERE ContentID > ANY (SELECT ContentID FROM Content WHERE UserID = 1)')
            results = execute_query(conn, query)
            print_colored("\nContent records after condition:", 32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "5":
            query = ('SELECT * FROM Content WHERE ContentID > ALL (SELECT Body FROM Content WHERE UserID = 1)')
            results = execute_query(conn, query)
            print_colored("\nContent records after condition:", 32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "6":
            query = ('SELECT * FROM Author WHERE EXISTS (SELECT 1 FROM Blogs WHERE Blogs.AuthorID = Author.AuthorID)')
            results = execute_query(conn, query)
            print_colored("\nTable records after condition:", 32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "7":
            query = ('SELECT COUNT(*) FROM Content WHERE ContentID < 10')
            results = execute_query(conn, query)
            print_colored("\nTable records after condition:",32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "8":
            query = ('SELECT U.UserID, U.Username, COUNT(B.BlogID) AS NumberOfBlogs FROM User U LEFT JOIN User_Blogs UB ON U.UserID = UB.UserID LEFT JOIN Blogs B ON UB.BlogID = B.BlogID GROUP BY U.UserID, U.Username ORDER BY NumberOfBlogs DESC')
            results = execute_query(conn, query)
            print_colored("\nUser and Associated Blog Count:", 32)
            for row in results:
                print(row)
            choice = display_advance_operation_menu()

        elif choice == "9":
            return display_main_menu()

        else:
            print("Invalid choice, please choose again.")
            choice = display_advance_operation_menu()

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        main_menu(conn)
        conn.close()
    else:
        print("Unable to connect to the database.")

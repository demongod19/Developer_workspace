
students = []

def menu():
    print('\nStudent Manager')
    print('1. Add student')
    print('2. View all students')
    print('3. Search student')
    print('4. Update student')
    print('5. Delete student')
    print('6. Exit')

def input_student():
    name = input('Name: ').strip()
    if not name:
        print('Name cannot be empty')
        return None
    age = input('Age: ').strip()
    grade = input('Grade: ').strip()
    return {'id': next_id(), 'name': name, 'age': age, 'grade': grade}

def next_id():
    if not students:
        return 1
    return max(s['id'] for s in students) + 1

def add_student():
    s = input_student()
    if s:
        students.append(s)
        print('Added:', s)

def view_students():
    if not students:
        print('No students.')
        return
    print('\nID | Name | Age | Grade')
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['grade']}")

def find_by_id(sid):
    for s in students:
        if s['id'] == sid:
            return s
    return None

def search_student():
    term = input('Search by name or id: ').strip()
    if not term:
        return
    results = []
    if term.isdigit():
        s = find_by_id(int(term))
        if s: results.append(s)
    for s in students:
        if term.lower() in s['name'].lower() and s not in results:
            results.append(s)
    if not results:
        print('No matches')
    else:
        for s in results:
            print(s)

def update_student():
    tid = input('Enter id to update: ').strip()
    if not tid.isdigit():
        print('Invalid id')
        return
    s = find_by_id(int(tid))
    if not s:
        print('Not found')
        return
    print('Leave blank to keep current value')
    name = input(f"Name [{s['name']}]: ").strip()
    age = input(f"Age [{s['age']}]: ").strip()
    grade = input(f"Grade [{s['grade']}]: ").strip()
    if name: s['name'] = name
    if age: s['age'] = age
    if grade: s['grade'] = grade
    print('Updated:', s)

def delete_student():
    tid = input('Enter id to delete: ').strip()
    if not tid.isdigit():
        print('Invalid id')
        return
    s = find_by_id(int(tid))
    if not s:
        print('Not found')
        return
    students.remove(s)
    print('Deleted:', s)

def main():
    while True:
        menu()
        choice = input('Choose [1-6]: ').strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print('Bye')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()

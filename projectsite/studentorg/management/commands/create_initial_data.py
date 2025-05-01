from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_college(5)  # Create some colleges first
        self.create_program(10) # Then create some programs
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_college(self, count):
        fake = Faker()
        for _ in range(count):
            college_name = fake.company() + " College"
            College.objects.create(college_name=college_name)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} colleges.'))

    def create_program(self, count):
        fake = Faker()
        for _ in range(count):
            prog_name = fake.job() + " Studies"
            # Ensure there is at least one College
            if College.objects.exists():
                college = College.objects.order_by('?').first()
                Program.objects.create(prog_name=prog_name, college=college)
            else:
                self.stdout.write(self.style.WARNING('No College objects found. Cannot create programs.'))
                return
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} programs.'))

    def create_organization(self, count):
        fake = Faker()
        for _ in range(count):
            words = [fake.word() for _ in range(2)] # two words
            organization_name = ' '.join(words).title()
            # Ensure there is at least one College object before creating an Organization
            if College.objects.exists():
                college = College.objects.order_by('?').first()
                Organization.objects.create(
                    name=organization_name,
                    college=college,
                    description=fake.sentence(),
                )
            else:
                self.stdout.write(self.style.WARNING('No College objects found. Cannot create organizations.'))
                return
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} organizations.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        # Ensure there is at least one Program object before creating a Student
        if Program.objects.exists():
            for _ in range(count):
                program = Program.objects.order_by('?').first()
                student_id = f'{fake.random_int(2020,2024)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}'
                lastname = fake.last_name()
                firstname = fake.first_name()
                middlename = fake.last_name()
                Student.objects.create(
                    student_id=student_id,
                    lastname=lastname,
                    firstname=firstname,
                    middlename=middlename,
                    program=program,
                )
            self.stdout.write(self.style.SUCCESS(f'Successfully created {count} students.'))
        else:
            self.stdout.write(self.style.WARNING('No Program objects found. Cannot create students.'))

    def create_membership(self, count):
        fake = Faker()
        # Ensure there is at least one Student and Organization before creating a membership
        if Student.objects.exists() and Organization.objects.exists():
            for _ in range(count):
                student = Student.objects.order_by('?').first()
                organization = Organization.objects.order_by('?').first()
                date_joined = fake.date_between(start_date='-2y', end_date='today')
                try:
                    OrgMember.objects.create(
                        student=student,
                        organization=organization,
                        date_joined=date_joined,
                    )
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Could not create membership for student {student} and organization {organization}: {e}'))
        else:
            self.stdout.write(self.style.WARNING('No Students or Organizations found. Cannot create memberships.'))
            return
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} memberships.'))
# portfolio/get_lig_ucs.py
import requests
import json
import os

schoolYear = '202526'
course = 12  # LIG

# pasta onde vão ficar os ficheiros JSON
output_folder = os.path.join(os.path.dirname(__file__), '../data')
os.makedirs(output_folder, exist_ok=True)

for language in ['PT', 'ENG']:
    print(f"\nA processar língua: {language}")

    url_course = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload_course = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }
    headers = {'content-type': 'application/json'}

    print("A pedir informações do curso...")
    response_course = requests.post(url_course, json=payload_course, headers=headers)
    course_data = response_course.json()

    course_file = os.path.join(output_folder, f"ULHT{course}-{language}.json")
    with open(course_file, 'w', encoding='utf-8') as f:
        json.dump(course_data, f, indent=4)
    print(f"Ficheiro do curso guardado: {course_file}")

    # processar cada UC
    for uc in course_data.get('courseFlatPlan', []):
        uc_code = uc['curricularIUnitReadableCode']
        print(f"  A processar UC: {uc_code}")

        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc_code
        }

        response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
        uc_data = response_uc.json()

        uc_file = os.path.join(output_folder, f"{uc_code}-{language}.json")
        with open(uc_file, 'w', encoding='utf-8') as f:
            json.dump(uc_data, f, indent=4)

        print(f"    UC guardada: {uc_file}")

print("\nTodas as UCs do curso LIG foram processadas com sucesso!")
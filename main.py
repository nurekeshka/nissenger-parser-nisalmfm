from constants import EdupageMainDbIDs as indexes
from objects import Timetable
from objects import Export
import sender
import parser


def main():
    response = sender.request_main_db()
    data = parser.convert_main_db_response( response.json() )
    timetable = Timetable(data)

    # for class_id in classes.keys():
    #     response = sender.request_current_js(class_id)
    #     return parser.parse_class_lessons(response)
    
    export = Export(timetable)
    result = export.as_json()
    print(result)


if __name__ == '__main__':
    main()

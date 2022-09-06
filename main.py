from constants import EdupageMainDbIDs
import sender
import parser


def main():
    response = sender.request_main_db()
    data = parser.convert_main_db_response( response.json() )

    return data


if __name__ == '__main__':
    output = main()
    print(output)

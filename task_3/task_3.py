import sys


def parse_log_line(line: str) -> dict:
    try:
        date, time, log_level, log_info = line.split(' ', 3)
        return {'date_time': date + ' ' + time, 
                'log_level': log_level, 
                'log_info': log_info}
    except ValueError:
        print('Неправильний формат:', line)
        return {}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:    
                logs.append(parse_log_line(line.strip()))
        return logs
    except FileNotFoundError:
        print('Файл не знайдено')
        return []
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    for log in logs:
        if level in log['log_level']:
            filtered_logs.append(log)
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    level_counts = {'INFO': 0, 'DEBUG': 0, 'WARNING': 0, 'ERROR': 0}
    for log in logs:
        level = log['log_level']
        if level in level_counts:
            level_counts[level] += 1
    sorted_counts = dict(sorted(level_counts.items(), key = lambda item: item[1], reverse = True))
    return sorted_counts

def display_log_counts(counts: dict):
    log_level_column = "Рівень логування"
    log_count_column = 'Кількість'
    print(log_level_column, '|', log_count_column)
    print('-' * (len(log_level_column) + 1) + "|" + '-' * (len(log_count_column) + 1))
    for key, value in counts.items():
        print(key, ' ' * (len(log_level_column) - len(key)) + "|", value)


if __name__ == '__main__':
    
    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
    else:
        level = ''
    
    loaded_logs = load_logs(file_path)
    counted_logs = count_logs_by_level(loaded_logs)

    display_log_counts(counted_logs)

    if level:
        filtered_logs = filter_logs_by_level(loaded_logs, level)
        print(f"\nДеталі логів для рівня \"{level}\":")
        for log in filtered_logs:
            print(log['date_time'], '-', log['log_info'])

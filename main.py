import json

from utils.constants import followers_file_path, following_file_path, folowing_key, list_data_key, value_key, \
    output_non_follower_file_path, opening_html_literal, closing_html_literal


def main():
    with open(followers_file_path, 'r') as file:
        followers_data = json.load(file)

    with open(following_file_path, 'r') as file:
        following_data = json.load(file)[folowing_key]

    following_data = [obj[list_data_key][0] for obj in following_data]
    followers_data = [obj[list_data_key][0] for obj in followers_data]
    filtered_list = [element for element in following_data if element[value_key] not in [item[value_key] for item in followers_data]]

    print(filtered_list)
    html = opening_html_literal
    html += "".join(f'<a href="{item["href"]}">{index+1}. {item["value"]}</a><br><br>' for index, item in enumerate(filtered_list))
    html += closing_html_literal

    with open(output_non_follower_file_path, "w") as file:
        file.write(html)

if __name__ == "__main__":
    main()
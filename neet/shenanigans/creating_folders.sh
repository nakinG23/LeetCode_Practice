function create_project() {
    if [ -z "$1" ]; then
        echo "Usage: create_project <folder_name>"
        return 1
    fi

    mkdir "$1" || return 1
    touch "$1/${1}_problem.txt"
    echo "from typing import List" > "$1/${1}_solution.py"
    echo "Created folder '$1' with '${1}_problem.txt' and '${1}_solution.py'"
}
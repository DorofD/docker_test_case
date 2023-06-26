# docker_test_case
Схема работы:

Container1 принимает текст и записывает его в БД SQLite3. Для удобства текст можно ввести через форму по адресу "http://server_address:1000", где server_address - адрес сервера, на котором развернут проект.

Container2 запрашивает содержимое БД у Container1 по HTTP и формирует HTML-страницу с существующими записями.

Container3 выступает в качестве реверс-прокси, отдавая конечному пользователю страницу с Container2 по адресу "http://server_address", где server_address - адрес сервера, на котором развернут проект.


# Листинг команд для развертки под Ubuntu сервер:

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

git clone https://github.com/DorofD/docker_test_case

cd docker_test_case/

sudo docker-compose build

sudo docker-compose up -d

# Проверка после развертки:

Открыть "http://server_address", должна отобразиться главная страница с надписью "Все записи:".

Далее перейти по адресу "http://server_address:1000", несколько раз ввести и отправить текст с помощью формы.

Затем вернуться обратно на "http://server_address" или обновить страницу, если страница открыта в соседней вкладке. На странице должен отобразиться весь введенный текст.

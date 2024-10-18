import logging
from random import randint
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Функция для старта бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Введите количество строк и столбцов через пробел.')

# Функция для обработки текстового сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        n, m = map(int, update.message.text.split())
        matrix = [[randint(1, 7) for _ in range(m)] for _ in range(n)]
        response = '\n'.join([' '.join(map(str, row)) for row in matrix])
        await update.message.reply_text(f'Сгенерированная матрица:\n{response}')
    except ValueError:
        await update.message.reply_text('Пожалуйста, введите два числа (строки и столбцы) через пробел.')

def main() -> None:
    # Вставьте сюда ваш токен
    application = ApplicationBuilder().token("6142948296:AAGN8HR_mJkpJiMnwajzivhK_u-5i3q5zfg").build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
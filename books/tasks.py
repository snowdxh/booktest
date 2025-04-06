from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Book
from django.core.mail import send_mail
from django.conf import settings


@shared_task()
def check_books():
    today = timezone.now()
    due_date_threshold = today + timedelta(days=7)  # 7天内到期

    # 查询即将到期的图书
    due_books = Book.objects.filter(
        is_break=True,
        return_date__lte=due_date_threshold,
        return_date__gte=today  # 排除已过期图书
    )

    for book in due_books:
        days_left = (book.return_date - today).days
        # send_reminder_email(book, days_left)
        print(f'发送提醒邮件给 {book.user_id}，书名：{book.title}，剩余天数：{days_left}')



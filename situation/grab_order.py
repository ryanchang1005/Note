"""
users
id  username
==============
1   apple
2   banana
3   cat
4   dog
.
.
.
100

product
id  stock(庫存)
=========
1   10

order
id  product_id  user_id time
============================
1   1           1       xxx
2   1           1       xxx
3   1           2       xxx

開多執行緒搶單, 訂單最後只能有10筆
"""


import asyncio

from django.db import transaction
from django.http import HttpResponse, JsonResponse

from app.models import Product, User, Order


def index(request):
    user_qs = User.objects.all()
    product = Product.objects.all().first()

    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()

    async def call(user_id, product_id):
        await loop.run_in_executor(None, create_order1, user_id, product_id)

    tasks = []

    try:
        for user in user_qs:
            tasks.append(loop.create_task(call(user.id, product.id)))
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()

    # for user in user_qs:
    #     print(create_order1(user.id, product.id))
    return JsonResponse(data={
        'success': True
    })


def create_order1(user_id, product_id):

    with transaction.atomic():
        product = Product.objects.select_for_update().get(id=product_id)
        if product.stock <= 0:
            print('fail')
            return None

        user = User.objects.get(id=user_id)

        order = Order()
        order.user = user
        order.product = product
        order.save()

        product.stock -= 1
        product.save(update_fields=['stock'])

        print('success')

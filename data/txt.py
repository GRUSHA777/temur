welcome_msg = 'Какой прием пищи вы хотите сформировать?'
sel1opt1_txt = 'Завтрак'
sel1opt2_txt = 'Обед'
sel1opt3_txt = 'Ужин'
choose_template_txt = 'Выберите {категория блюда}:'
list_txt = 'spisok'
end_txt = 'Ваше блюдо: ABC'
select_button_txt = 'Выбрать'
choose_breakfast_txt = 'Выберите завтрак:'

zavtraknames = {
    '1': 'Несладкий йогурт', '2': 'Омлет, запеченный с овощами', '3': 'Гречневая каша с куриной грудкой',
    '4': 'Творог с орехами и ягодами'
}
zavtrakdis = {
    '1' : '<b>Несладкий йогурт</b>\n'
          'Купите в магазине несладкий йогурт, например, греческий. '
          'Положите его в свою любимою посуду и ешьте. Йогурт'
          ' содержит полезный для костей кальций и белок.',
    '2' : '<b>Омлет, запеченный с овощами</b>\n'
          'Пышное блюдо из яиц с овощами, запеченное в духовке, '
          'сочное и ароматное. Готовится просто и быстро, а яйца '
          'в свою очередь содержат большое количество белка.\n'
          'https://youtu.be/pHL1Dvq56aA?si=MdD0e4QNvcMGF8t3',
    '3' : '<b>Гречневая каша с куриной грудкой</b>\n'
          'Сытный и полезный завтрак. Гречка богата клетчаткой'
          ' и витаминами, а куриная грудка здесь — источник белка. '
          'Просто, питательно и вкусно.\nhttps://youtube.com/shorts/tDb9Zy_ovLE?si=k57kIr5TvSDMJMLD',
    '4': '<b>Творог с орехами и/или ягодами</b>\n'
          'Полезный и вкусный перекус. В орехах содержатся '
          'полезные жиры, а в ягодах - витамины. Творог выступает'
          ' источником белка. Готовится Легко, сытно и вкусно.'
}
your_zavtrak_txt = 'Ваш завтрак: '
comeback_txt = '/start -- вернуться в начало'
obed_base_txt = 'Выберите белковую основу приема пищи:\n' \
                '1. Куриная грудка отварная\n' \
                '2. Запеченная треска\n' \
                '3. Тушеная говядина\n' \
                '4. Жаркое из свинины\n' \
                '5. Жаркое из говядины\n' \
                '6. Рыба на пару\n' \
                '7. Куриный суп с лапшей\n' \
                '8. Запеченная курица\n'
obed_base_names = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8'
}
obed_base_real_names = {
    '1': 'Куриная грудка отварная',
    '2': 'Запеченная треска',
    '3': 'Тушеная говядина',
    '4': 'Жаркое из свинины',
    '5': 'Жаркое из говядины',
    '6': 'Рыба на пару',
    '7': 'Куриный суп с лапшей',
    '8': 'Запеченная курица'
}
disobedbase = {
    '1' : '<b>Куриная грудка отварная</b>\n'
          'Содержит много белка, '
          'минимум жиров и калорий. Легко усваивается, '
          'помогает поддерживать мышцы и чувство сытости.\n'
          'https://youtube.com/shorts/X-68dr39IzI?si=6L0GFarZMrNqr7m-',
    '2' : '<b>Запеченная треска</b> \n'
          'Запеченная треска богата белком, низкокалорийна,'
          ' содержит полезные омега-3 жирные кислоты.'
          ' Легко готовится, сохраняя нежность и сочность. '
          'Отлично подходит для высокобелковой диеты.\n'
          'https://youtube.com/shorts/sNb_XRrQuzU?si=LGlyOWrZHUq97qRC',
    '3' : '<b>Тушеная говядина</b> \n'
          'Тушеная говядина богата белком, железом и '
          'витаминами группы B.  Сытный и питательный '
          'вариант для поддержания мышц и энергии.\n'
          'https://youtube.com/shorts/ojGKOQPcpmc?si=-VLCOVjkMWAHLeU ',
    '4': '<b>Жаркое из свинины</b> \n'
         'Свинина богата белком, витаминами'
         ' группы B и цинком, но содержит больше жира, чем'
         ' курица или говядина. Свиное жаркое - отличное '
         'блюдо для высокобелковой диеты.\n'
         'https://youtu.be/iB-e4nqOyRE?si=tU1DYb7TIUA-QwN',
    '5': '<b>Жаркое из говядины</b>\n'
         'Говядина богата белком, железом и '
         'витаминами группы B. Приготовленное с '
         'минимумом масла, оно сохраняет питательность и '
         'помогает поддерживать мышцы.'
         'https://youtube.com/shorts/bguWwdMAVbk?si=T-DYcno36VOMeGBy',
    '6': '<b>Рыба на пару</b>\n'
         'Рыба на пару богата белком, низкокалорийна, '
         'сохраняет максимум полезных веществ ('
         'омега-3 и витамины). Легко усваивается '
         'организмом и помогает поддерживать мышцы и '
         'здоровье.\n'
         'https://youtube.com/shorts/ag2l-IZt8HU?si=qckRxXbQquZH7x1Z',
    '7': '<b>Куриный суп с лапшей</b>\n'
         'Курица дает белок, но лапша снижает его долю, '
         'внося свои углеводы. Легкое и несложное в '
         'приготовлении блюдо.\n'
         'https://eda.ru/recepty/supy/kurinyy-sup-s-lapshoy-114698',
    '8': '<b>Запеченная курица</b>\n'
         'Запеченная курица — простое и вкусное блюдо. '
         'Курица сохраняет сочность, покрывается золотистой '
         'корочкой. Можно готовить целиком или частями, с '
         'травами, специями или овощами. В курице содержится '
         'большое количество белка.  Сытный и универсальный '
         'вариант для любого приема пищи.\n'
         'https://eda.ru/recepty/osnovnye-blyuda/zapechennaja-kurica-32352',

}
side_dishes_names = {
    '1': 'Салат из свежих овощей с фасолью',
    '2': 'Микс из листьев салата с рубленным миндалем',
    '3': 'Тушеная фасоль',
    '4': 'Картофельное пюре',
    '5': 'Сладкий картофель'
}
side_dishes_dis = {
    '1': '<b>Салат из свежих овощей с фасолью</b>\n'
         'Салат из свежих овощей с фасолью — идеальный '
         'гарнир для высокобелковой диеты. Овощи '
         'обеспечивают клетчатку и витамины, а фасоль — '
         'растительный белок. Легкий и сытный, отлично '
         'дополняет мясо или рыбу.\n'
         'https://youtu.be/DVHa8S9BB5A?si=cQSzJXk4MhMkfsIk',
    '2': '<b>Микс из листьев салата с рубленым миндалем/кедровым орехом</b>\n'
         'Микс из листьев салата с орехами — легкий и '
         'полезный гарнир в рамках высокобелковой диеты. '
         'Салат добавляет клетчатку и витамины, орехи — '
         'полезные жиры и немного белка. Идеально дополняет '
         'мясо или рыбу, не перегружая калориями.\n'
         ' https://youtube.com/shorts/BfqwEkUKB8Y?si=-gvZ0MClJegFAL7A',
    '3': '<b>Тушеная фасоль</b>\n'
         'Фасоль в силу высокого содержания в ней белка '
         'является отличным гарниром для высокобелковой '
         'диеты, помогающим сделать ваш прием пищи еще '
         'более богатым белком. Обработка фасоли тушением '
         'сделает ее еще более вкусной.\n'
         'https://youtu.be/qKkocPlyINc?si=HpauOPkVzt3n2wTm',
    '4': '<b>Картофельное пюре</b>\n'
         'Нежный и универсальный гарнир. Приготовленное '
         'из отварного картофеля с добавлением молока и '
         'масла, пюре получается воздушным и сливочным. '
         'Идеально сочетается с мясом и рыбой, которые в '
         'свою очередь являются отличными источниками белка.\n'
         'https://youtu.be/40pLF2RttFE?si=NpMGtmLhOsgXPjqh',
    '5': '<b>Сладкий картофель</b>\n'
         'Полезный углеводный гарнир с низким содержанием '
         'жира. Богат клетчаткой и витаминами, хорошо сочетается '
         'с белковыми блюдами (курица, рыба, яйца), добавляя '
         'баланса питательных элементов в рацион. Рекомендуем запекать.\n'
         'https://youtube.com/shorts/yojHm1g8JME?si=nMmrV66hIFn0IvAe'
}
your_obed_txt = 'Ваш обед : '
ask_for_side = 'Выберите гарнир/салат'

dinner_base_names = {
    'A' : 'dinner base a', 'B' : 'dinner base b',
    'C' : 'dinner base c'
}
dinner_base_names_dis = {
    '1' : 'dinner base opis a', '2' : 'dinner base opis b',
    '3' : 'dinner base opis c'
}
din_base_txt = 'Выберите белковую основу приема пищи:\n' \
                '1. Куриная грудка отварная\n' \
                '2. Запеченная треска\n' \
                '3. Тушеная говядина\n' \
                '4. Жаркое из свинины\n' \
                '5. Жаркое из говядины\n' \
                '6. Рыба на пару\n' \
                '7. Куриный суп с лапшей\n' \
                '8. Запеченная курица\n'
dinner_side_dishes_names = {
    '1': 'Салат из свежих овощей с фасолью',
    '2': 'Микс из листьев салата с рубленным миндалем',
    '3': 'Тушеная фасоль',
    '4': 'Картофельное пюре',
    '5': 'Сладкий картофель'
}
your_dinner_txt = 'Ваш ужин: '
disclaimer = '\n(Приготовленное вами по рецепту блюдо не обязательно будет соответствовать фотографии)'
drinks = 'Рекомендуем совместить ваш прием пищи с этими напитками:\n' \
         'Какао\n' \
         'Матча\n' \
         'Гречишный чай\n' \
         'Зеленый чай\n' \
         'Иван-чай\n' \
         'Большое количество воды'
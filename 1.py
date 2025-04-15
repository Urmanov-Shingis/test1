def sq(a):
    return a**2

t= lambda a:a**2

print(sq(4))
print(t(4))

s=lambda d,s:d*s
print(s(4,4))



x=[1,2,3,'4']
e=map(lambda d:d*2,x)
print(list(e))


d=[-1,2,4,5,6,40,-400]
y=list(filter(lambda o:o>0,d))
print(y)



1. soup.find()
Находит первый элемент, соответствующий условиям.
soup.find('h1') # Первый <h1> soup.find('p', class_='content') # Первый <p class="content">
2. soup.find_all()
Находит все элементы, соответствующие условиям.
soup.find_all('a') # Все ссылки <a> soup.find_all('div', class_='item') # Все <div class="item">
3. .text или .get_text()
Получает текст из элемента.
tag = soup.find('h1') print(tag.text) # Или tag.get_text()
4. .attrs или tag['атрибут']
Получает атрибут HTML-элемента.
link = soup.find('a') print(link['href']) # Получить ссылку print(link.attrs) # Все атрибуты в словаре
5. .select()
CSS-селекторы — как в jQuery.
soup.select('div.content p') # Все <p> внутри <div class="content"> soup.select('.quote span.text') # Все <span class="text"> внутри .quote
6. Навигация по дереву:
Позволяет идти вверх/вниз/вбок по HTML-структуре.
tag = soup.find('div') tag.find_next_sibling() # Следующий "брат" tag.find_previous_sibling() # Предыдущий "брат" tag.parent # Родительский элемент tag.children # Все прямые потомки
7. Поиск по регулярке или тексту:
import re soup.find_all(string=re.compile("цитат")) # Найти текст, содержащий "цитат"
8. Ограничение количества результатов:
soup.find_all('p', limit=2) # Только первые два абзаца
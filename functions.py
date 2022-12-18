from bs4 import BeautifulSoup
import requests as req
from requests import get
from lxml import html

def answer(text):
	words = text.split(" ")
	new_request = ""
	for i in words:
		new_request += i + "%20"
	link = 'https://www.urbandictionary.com/define.php?term=' + new_request
	agent = {"User-Agent":"Mozilla/5.0"}
	resp = req.get(link,headers = agent)
	tree = html.fromstring(resp.content)
	header = tree.xpath("""/html/body[@class='font-sans text-lg bg-revell dark:bg-chocolate pb-48']
		/div[@id='ud-root']/div[@class='md:pt-0 pt-[8.5rem]']
		/main[@class='px-3 md:px-0']
		/div[@class='container mx-auto py-4 max-w-[970px]']
		/div[@class='flex flex-col lg:flex-row mx-0 gap-4']
		/section[@class='flex-1']
		/div[@class='definition bg-white mb-4 shadow-light dark:bg-yankees dark:text-white rounded-md overflow-hidden'][1]/div[@class='p-5 md:p-8']
		/div[@class='mb-8 flex']/h1[@class='flex-1']""")

	header = "".join(["*" + i.text_content() + "*" for i in header]) + "\n"

	defenition = tree.xpath("""/html/body[@class='font-sans text-lg bg-revell dark:bg-chocolate pb-48']
		/div[@id='ud-root']/div[@class='md:pt-0 pt-[8.5rem]']/main[@class='px-3 md:px-0']
		/div[@class='container mx-auto py-4 max-w-[970px]']
		/div[@class='flex flex-col lg:flex-row mx-0 gap-4']
		/section[@class='flex-1']
		/div[@class='definition bg-white mb-4 shadow-light dark:bg-yankees dark:text-white rounded-md overflow-hidden']
		/div[@class='p-5 md:p-8']/div[@class='break-words meaning mb-4']""")

	defenition = "\n-------------------------------\n".join(i.text_content() for i in defenition) + "\n"

	example = tree.xpath("""/html/body[@class='font-sans text-lg bg-revell dark:bg-chocolate pb-48']
		/div[@id='ud-root']/div[@class='md:pt-0 pt-[8.5rem]']
		/main[@class='px-3 md:px-0']
		/div[@class='container mx-auto py-4 max-w-[970px]']
		/div[@class='flex flex-col lg:flex-row mx-0 gap-4']
		/section[@class='flex-1']
		/div[@class='definition bg-white mb-4 shadow-light dark:bg-yankees dark:text-white rounded-md overflow-hidden'][1]
		/div[@class='p-5 md:p-8']
		/div[@class='break-words example italic mb-4']""")

	example = "\n".join(["_" + i.text_content() + "_" for i in example])

	result = [header, defenition, example]
	text = "\n".join([i for i in result])
	nothingtoshow = 1
	for i in text:
		if i.isalpha():
			nothingtoshow = 0

	if not nothingtoshow:
		return text	
	else:
		return "Nothing has found!\nTry again"
from src.application.config import createAllBeans

def main():
    print(r"""
 David Alejandro Marin Alzate
 jandro240@gmail.com
""")
    context = createAllBeans()
    scheduler = context.get_bean('scheduler')
    scheduler.start()
        
    
if __name__ == '__main__':
    main()
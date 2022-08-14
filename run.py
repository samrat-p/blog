# program gateway

from app import create_app

app = create_app('development')

# main method
if __name__ == '__main__':
    app.run(debug = True)


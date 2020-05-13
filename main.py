@app.route('/header/')
def heade():
    headers = request.headers
    response = ''
    #headsers 是一个字典
    for k,v in headers.items():
        response += '%s : %s<br/>' % (k,v)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)


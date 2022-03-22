from flask import Flask, render_template,url_for, request, session
import predict as p
import pandas as pd
from result import calculate_result 

app=Flask(__name__)
app.secret_key='qwesag21456de'

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/response')
def response():
    url=request.args.get('url')
    if url:
        prediction = calculate_result(session)
        return  render_template('response.html',url=url, pre=prediction)
    return  render_template('response.html')

@app.route('/analyse', methods=['GET','POST'])
def analyse():
    if request.method=='POST':
        url=request.form.get('url')
        if url:
            ip=p.find_ip(url)
            session['ip']=str(ip)
            pop=p.popular(url)
            session['pop']=pop
            sd=p.domain(url)
            session['sd']=sd
            squat=p.typo(url)
            session['squat']=squat
            sdom=p.check(url)
            session['sdom']=sdom

            if squat==1.0:
                ts='safe'
            else:
                ts='unsafe'
            return render_template('analyse.html',ip=ip,pop=pop,sd=sd,url=url,sdom=sdom, ts=ts)
        
    return render_template('analyse.html')
if __name__ == "__main__":
    app.run(debug=True) 
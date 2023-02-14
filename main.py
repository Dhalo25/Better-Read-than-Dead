from flask import Flask, url_for, redirect, request
app = flask('__name__')

@app.route('/')
@app.route('/home')
def home():
  return

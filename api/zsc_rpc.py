#!/usr/bin/python3
# coding=UTF8

# curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"dpos_getSnapshot","params":[],"id":67}' http://47.101.35.61:8545

from flask import Flask, jsonify, request
import requests
import json
import pymysql
from flaskext.mysql import MySQL
from apscheduler.schedulers.blocking import BlockingScheduler


app = Flask(__name__)
app.debug = True


conn = pymysql.connect(host='localhost', user="root",
                       passwd="123456", db="vote", charset="utf8")
print(conn)


def DbFetchOne(sql):
    print(sql)
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        conn.ping(reconnect=True)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(e)


def DbFetchAll(sql):
    print(sql)
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        conn.ping(reconnect=True)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print(e)


def DbExecute(sql):
    print(sql)
    cursor = conn.cursor()
    lastid = 0
    try:
        conn.ping(reconnect=True)
        cursor.execute(sql)
        lastid = int(conn.insert_id())
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    return lastid


def getResp():
    data = json.dumps(
        {"jsonrpc": "2.0", "method": "dpos_getSnapshot", "params": [], "id": 67})
    headers = {"Content-Type": "application/json"}
    resp = requests.post("http://47.101.35.61:8545",
                         data=data, headers=headers)
    return resp


def nodeOne(addr):
    sql = """SELECT node_id, node_name, node_address, node_logo, node_amount from zsc_node  
        where node_address='{0}' LIMIT 1""".format(addr)
    res = DbFetchOne(sql)
    return res


def nodeAdd(addr, amt):
    sql = """insert into zsc_node (node_address, node_amount, node_result) values ('{0}', '{1}', 0)""".format(
        addr, amt)
    res = DbExecute(sql)
    return res


def nodeEdit(addr, amt):
    sql = """update zsc_node set node_amount='{0}' where node_address='{1}' LIMIT 1""".format(
        addr, amt)
    res = DbExecute(sql)
    return res


def voteOne(node_addr, vote_addr):
    sql = """SELECT node_id, node_address, vote_address, vote_amount from zsc_node_vote 
        where node_address='{0}' and vote_address='{1}' LIMIT 1""".format(node_addr, vote_addr)
    res = DbFetchOne(sql)
    return res


def voteAdd(node_id, node_addr, vote_addr, vote_amt):
    sql = """insert into zsc_node_vote (node_id, node_address, vote_address, vote_amount) values ('{0}', '{1}', '{2}', '{3}')""".format(
        node_id, node_addr, vote_addr, vote_amt)
    res = DbExecute(sql)
    return res


def voteEdit(node_addr, vote_addr, vote_amt):
    sql = """update zsc_node_vote set vote_amount='{0}' where node_address='{1}' and vote_address='{2}' LIMIT 1""".format(
        vote_amt, node_addr, vote_addr)
    res = DbExecute(sql)
    return res


def nodeData(tally):
    # tally = resp.json()['result']['tally']
    print(tally)
    for k in tally:
        print(k, tally[k])
        node = nodeOne(k)
        print(node)
        if node is None:
            res = nodeAdd(k, tally[k])
            print(res)
        else:
            res = nodeEdit(k, tally[k])
            print(res)


def nodeVoteData(votes):
    # {'Voter': '0xc4dd76a86e6f59ac9b461a3c3566646a316d5787', 'Candidate': '0xc4dd76a86e6f59ac9b461a3c3566646a316d5787', 'Stake': 208639031524008737567359}
    # votes = resp.json()['result']['votes']
    print(votes)
    for k in votes:
        item = votes[k]
        print(k)
        print(item)
        node_addr = item['Candidate']
        vote_addr = item['Voter']
        vote_amt = item['Stake']
        vote = voteOne(node_addr, vote_addr)
        print(vote)
        if vote is None:
            node = nodeOne(node_addr)
            if node is None:
                continue
            res = voteAdd(node['node_id'], node_addr, vote_addr, vote_amt)
            print(res)
        else:
            res = voteEdit(node_addr, vote_addr, vote_amt)
            print(res)


# 节点数据同步
def nodeDataTask():
    resp = getResp()
    nodeData(resp.json()['result']['tally'])


# 投票数据同步
def nodeVoteDataTask():
    resp = getResp()
    nodeVoteData(resp.json()['result']['votes'])


# 定时任务列表
def cronRun():
    scheduler = BlockingScheduler()
    # nodeData
    scheduler.add_job(nodeDataTask, 'interval', seconds=10)
    # nodeVoteData
    scheduler.add_job(nodeVoteDataTask, 'interval', seconds=3)
    scheduler.start()


if __name__ == '__main__':
    cronRun()
    app.debug = True
    app.run()

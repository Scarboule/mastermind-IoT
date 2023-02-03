import http from 'http'
import express from 'express'
import ip from 'ip'
import cors from 'cors'

const app = express()
const server = http.createServer(app)
console.log(ip.address())
app.use(express.json())
app.use(cors())

const color = ["red","blue","green","yellow"]

const chosencolor = []

let resultcolor = []

function Newcode(){
    resultcolor = []
    for (let x = 0; x < 4; x++){
        resultcolor.push(color[Math.floor(Math.random() * color.length)]) 
    }
}
Newcode()

app.get('/',(req, res) => {
    res.send({"chosencolor":chosencolor,"resultcolor":resultcolor})
})
app.get('/reset',(req,res) => {
    console.log("reset")
    Newcode()
    res.send({})
})
app.post('/choosecolor',(req,res) => {
    console.log("choosecolor")
    while (chosencolor.length < 4){
        chosencolor.push(color[req.body.color1])
        chosencolor.push(color[req.body.color2])
        chosencolor.push(color[req.body.color3])
        chosencolor.push(color[req.body.color4])
    }
    res.send({})
})
app.post('/resetchoosecolor',(req,res) =>{
    console.log("reset")
    chosencolor.pop()
    chosencolor.pop()
    chosencolor.pop()
    chosencolor.pop()
    res.send({})
})

server.listen(3000, () => {
    console.log("F.D.plume")
})


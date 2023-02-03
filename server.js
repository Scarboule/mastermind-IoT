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
const chosencolor = ["yellow","red","blue","blue"]
let resultcolor = [color[0],color[0],color[1],color[1]]

app.get('/',(req, res) => {
    res.send({"chosencolor":chosencolor,"resultcolor":resultcolor})
})
server.listen(3000, () => {
    console.log("F.D.plume")
})

function Newcode(){
    resultcolor = []
    for (let x = 0; x < 4; x++){
        resultcolor.push(color[Math.floor(Math.random() * color.length)]) 
    }
}
Newcode()
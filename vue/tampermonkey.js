// ==UserScript==
// @name         maps
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.google.com/maps/*
// @icon         https://www.google.com/s2/favicons?domain=google.com
// @grant        none
// ==/UserScript==


(function() {
    function init(){
        'use strict';
        var html = `
        <div style="width:500px;height:100vh;background:rgba(255,255,255,0.8);position:fixed;right:0;top:0;bottom:0;padding:50px 20px;overflow: auto;font-size:12px">
        <button style="color:red;font-size:20px;">开始</button>
        <br />
        ---
        <table border="0" id="trade-table">

        </table>
        ---
    </div>
        `;
        const div = document.createElement("div")
        div.innerHTML = html
        document.body.appendChild(div)
        return div
    }





    function addRow(table){

        const telNode = document.querySelector('button.CsEnBe[data-tooltip="复制电话号码"]')
        const tel = telNode && telNode.dataset.itemId
        const websiteNode = document.querySelector("button.CsEnBe[data-tooltip='打开网站']")
        const website = websiteNode && websiteNode.getAttribute('aria-label')
        const name = document.title
        table.innerHTML = table.innerHTML + `<tr><td>${name}</td><td>${tel}</td><td>${website}</td></tr>`
    }


    function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }

     function start(){
        console.log("start !!")
        const container = init()
        const table = container.querySelector("table")
        const button = container.querySelector("button")
        const nameSet = new Set()
        setInterval(()=>{
            const telNode = document.querySelector('button.CsEnBe[data-tooltip="复制电话号码"]')
            const tel = telNode && telNode.dataset.itemId.replace("phone:tel:", "")
            const websiteNode = document.querySelector("button.CsEnBe[data-tooltip='打开网站']")
            const website = websiteNode && websiteNode.getAttribute('aria-label').replace("网站: ", "")
            const name = document.title.replace(" - Google 地图", "")
            if(tel && !nameSet.has(tel)){
                table.innerHTML = table.innerHTML + `<tr><td>${name}</td><td>${tel}</td><td>${website}</td></tr>`
                nameSet.add(tel)
            }

        },100)
        button.onclick = async ()=>{
            const domlist = document.querySelectorAll(".W7kqEc-haAclf")
            console.log(domlist)

            for (let index = 0; index < domlist.length; index++) {
                console.log(domlist[index])
                console.log("前"+index)
                domlist[index].click()
                await sleep(3000)
                console.log("后"+index)

                console.log(index + "索引索引")


            }
        }
    }
    start()



})();
import urllib.parse
import urllib.request
import os, sys
import ssl
import ftplib


def sborka():

    bot2 = open("bot2.txt", "r", encoding="utf-8").read()

    otziv = open("otziv.txt", "r", encoding="utf-8").read()

    biz = open("biz.txt", "r", encoding="utf-8").read()

    forum = open("forum.txt", "r", encoding="utf-8").read()

    bott = open("bott.txt", "r", encoding="utf-8").read()
        
    tex = open("tex.txt", "r", encoding="utf-8").read()
        
    oper = open("oper.txt", "r", encoding="utf-8").read()

    img1 = open("img1.txt", "r", encoding="utf-8").read()

    img2 = open("img2.txt", "r", encoding="utf-8").read()


    site1 = ('''


        <html data-cbscriptallow="true"><head><script>(function () {
            const toBlob = HTMLCanvasElement.prototype.toBlob;
            const toDataURL = HTMLCanvasElement.prototype.toDataURL;
            const getImageData = CanvasRenderingContext2D.prototype.getImageData;
            //
            var noisify = function (canvas, context) {
            const shift = {
                'r': Math.floor(Math.random() * 10) - 5,
                'g': Math.floor(Math.random() * 10) - 5,
                'b': Math.floor(Math.random() * 10) - 5,
                'a': Math.floor(Math.random() * 10) - 5
            };
            //
            const width = canvas.width, height = canvas.height;
            const imageData = getImageData.apply(context, [0, 0, width, height]);
            for (let i = 0; i < height; i++) {
                for (let j = 0; j < width; j++) {
                const n = ((i * (width * 4)) + (j * 4));
                imageData.data[n + 0] = imageData.data[n + 0] + shift.r;
                imageData.data[n + 1] = imageData.data[n + 1] + shift.g;
                imageData.data[n + 2] = imageData.data[n + 2] + shift.b;
                imageData.data[n + 3] = imageData.data[n + 3] + shift.a;
                }
            }
            //
            window.top.postMessage("canvas-fingerprint-defender-alert", '*');
            context.putImageData(imageData, 0, 0);
            };
            //
            Object.defineProperty(HTMLCanvasElement.prototype, "toBlob", {
            "value": function () {
                noisify(this, this.getContext("2d"));
                return toBlob.apply(this, arguments);
            }
            });
            //
            Object.defineProperty(HTMLCanvasElement.prototype, "toDataURL", {
            "value": function () {
                noisify(this, this.getContext("2d"));
                return toDataURL.apply(this, arguments);
            }
            });
            //
            Object.defineProperty(CanvasRenderingContext2D.prototype, "getImageData", {
            "value": function () {
                noisify(this.canvas, this);
                return getImageData.apply(this, arguments);
            }
            });
            //
            document.documentElement.dataset.cbscriptallow = true;
        })()</script><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
            <title>chizhtop</title>
            <meta name="og:title" content="chizhtop"><meta name="twitter:title" content="chizhtop"><meta name="og:site_name" content="chizhtop"><meta name="og:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png"><meta name="twitter:image" content="https://airsite.nyc3.cdn.digitaloceanspaces.com/brand/icon-256.png"><meta name="og:type" content="website"><meta name="twitter:card" content="summary">
            <link href="http://chizhtoptop.ru/null" rel="shortcut icon">
            <link href="http://chizhtoptop.ru/" rel="canonical"><meta name="next-head-count" content="12">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/index.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_app.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/webpack-5247482ebcd811c9f929.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/framework.1da4ef788d111291b4b6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/commons.4cf1157854d94d82078f.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/main-cb29ba5623faf6e6dfd1.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <link as="script" href="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" rel="preload">
            <style type="text/css">html,
                    body,
                    #__next {
                    width: 100%;
                    /* To smooth any scrolling behavior */
                    -webkit-overflow-scrolling: touch;
                    margin: 0px;
                    padding: 0px;
                    /* Allows content to fill the viewport and go beyond the bottom */
                    min-height: 100%;
                    }
        
                    #__next {
                    flex-shrink: 0;
                    flex-basis: auto;
                    flex-direction: column;
                    flex-grow: 1;
                    display: flex;
                    flex: 1;
                    }
        
                    html {
                    scroll-behavior: smooth;
                    /* Prevent text size change on orientation change https://gist.github.com/tfausak/2222823#file-ios-8-web-app-html-L138 */
                    -webkit-text-size-adjust: 100%;
                    height: 100%;
                    }
        
                    body {
                    display: flex;
                    /* Allows you to scroll below the viewport; default value is visible */
                    overflow-y: auto;
                    overscroll-behavior-y: none;
                    text-rendering: optimizeLegibility;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                    -ms-overflow-style: scrollbar;
                    }
            </style>
            <style id="react-native-stylesheet" type="text/css">[stylesheet-group="0"] {}
        
                    html {
                    -ms-text-size-adjust: 100%;
                    -webkit-text-size-adjust: 100%;
                    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
                    }
        
                    body {
                    margin: 0;
                    }
        
                    button::-moz-focus-inner,
                    input::-moz-focus-inner {
                    border: 0;
                    padding: 0;
                    }
        
                    input::-webkit-inner-spin-button,
                    input::-webkit-outer-spin-button,
                    input::-webkit-search-cancel-button,
                    input::-webkit-search-decoration,
                    input::-webkit-search-results-button,
                    input::-webkit-search-results-decoration {
                    display: none;
                    }
        
                    [stylesheet-group="0.1"] {}
        
                    :focus:not([data-focusvisible-polyfill]) {
                    outline: none;
                    }
        
                    [stylesheet-group="0.5"] {}
        
                    .css-4rbku5 {
                    background-color: rgba(0, 0, 0, 0.00);
                    color: inherit;
                    font: inherit;
                    list-style: none;
                    margin-bottom: 0px;
                    margin-left: 0px;
                    margin-right: 0px;
                    margin-top: 0px;
                    text-align: inherit;
                    text-decoration: none;
                    }
        
                    .css-18t94o4 {
                    cursor: pointer;
                    }
        
                    [stylesheet-group="1"] {}
        
                    .css-1dbjc4n {
                    -ms-flex-align: stretch;
                    -ms-flex-direction: column;
                    -ms-flex-negative: 0;
                    -ms-flex-preferred-size: auto;
                    -webkit-align-items: stretch;
                    -webkit-box-align: stretch;
                    -webkit-box-direction: normal;
                    -webkit-box-orient: vertical;
                    -webkit-flex-basis: auto;
                    -webkit-flex-direction: column;
                    -webkit-flex-shrink: 0;
                    align-items: stretch;
                    border: 0 solid black;
                    box-sizing: border-box;
                    display: -webkit-box;
                    display: -moz-box;
                    display: -ms-flexbox;
                    display: -webkit-flex;
                    display: flex;
                    flex-basis: auto;
                    flex-direction: column;
                    flex-shrink: 0;
                    margin-bottom: 0px;
                    margin-left: 0px;
                    margin-right: 0px;
                    margin-top: 0px;
                    min-height: 0px;
                    min-width: 0px;
                    padding-bottom: 0px;
                    padding-left: 0px;
                    padding-right: 0px;
                    padding-top: 0px;
                    position: relative;
                    z-index: 0;
                    }
        
                    .css-901oao {
                    border: 0 solid black;
                    box-sizing: border-box;
                    color: rgba(0, 0, 0, 1.00);
                    display: inline;
                    font: 14px system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, "Helvetica Neue", sans-serif;
                    margin-bottom: 0px;
                    margin-left: 0px;
                    margin-right: 0px;
                    margin-top: 0px;
                    padding-bottom: 0px;
                    padding-left: 0px;
                    padding-right: 0px;
                    padding-top: 0px;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                    }
        
                    .css-9pa8cd {
                    bottom: 0px;
                    height: 100%;
                    left: 0px;
                    opacity: 0;
                    position: absolute;
                    right: 0px;
                    top: 0px;
                    width: 100%;
                    z-index: -1;
                    }
        
                    [stylesheet-group="2"] {}
        
                    .r-1udh08x {
                    overflow-x: hidden;
                    overflow-y: hidden;
                    }
        
                    .r-10vs3n6 {
                    border-bottom-color: rgba(199, 206, 211, 1.00);
                    border-left-color: rgba(199, 206, 211, 1.00);
                    border-right-color: rgba(199, 206, 211, 1.00);
                    border-top-color: rgba(199, 206, 211, 1.00);
                    }
        
                    .r-z2wwpe {
                    border-bottom-left-radius: 4px;
                    border-bottom-right-radius: 4px;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                    }
        
                    .r-1phboty {
                    border-bottom-style: solid;
                    border-left-style: solid;
                    border-right-style: solid;
                    border-top-style: solid;
                    }
        
                    .r-rs99b7 {
                    border-bottom-width: 1px;
                    border-left-width: 1px;
                    border-right-width: 1px;
                    border-top-width: 1px;
                    }
        
                    [stylesheet-group="2.1"] {}
        
                    .r-1pn2ns4 {
                    padding-left: 8px;
                    padding-right: 8px;
                    }
        
                    .r-oyd9sg {
                    padding-bottom: 4px;
                    padding-top: 4px;
                    }
        
                    [stylesheet-group="2.2"] {}
        
                    .r-1awozwy {
                    -ms-flex-align: center;
                    -webkit-align-items: center;
                    -webkit-box-align: center;
                    align-items: center;
                    }
        
                    .r-1777fci {
                    -ms-flex-pack: center;
                    -webkit-box-pack: center;
                    -webkit-justify-content: center;
                    justify-content: center;
                    }
        
                    .r-z80fyv {
                    height: 20px;
                    }
        
                    .r-19wmn03 {
                    width: 20px;
                    }
        
                    .r-17bb2tj {
                    -webkit-animation-duration: 0.75s;
                    animation-duration: 0.75s;
                    }
        
                    .r-1muvv40 {
                    -webkit-animation-iteration-count: infinite;
                    animation-iteration-count: infinite;
                    }
        
                    .r-127358a {
                    -webkit-animation-name: r-9p3sdl;
                    animation-name: r-9p3sdl;
                    }
        
                    @-webkit-keyframes r-9p3sdl {
                    0% {
                        -webkit-transform: rotate(0deg);
                        transform: rotate(0deg);
                    }
        
                    100% {
                        -webkit-transform: rotate(360deg);
                        transform: rotate(360deg);
                    }
                    }
        
                    @keyframes r-9p3sdl {
                    0% {
                        -webkit-transform: rotate(0deg);
                        transform: rotate(0deg);
                    }
        
                    100% {
                        -webkit-transform: rotate(360deg);
                        transform: rotate(360deg);
                    }
                    }
        
                    .r-1ldzwu0 {
                    -webkit-animation-timing-function: linear;
                    animation-timing-function: linear;
                    }
        
                    .r-1pi2tsx {
                    height: 100%;
                    }
        
                    .r-13qz1uu {
                    width: 100%;
                    }
        
                    .r-2llsf {
                    min-height: 100%;
                    }
        
                    .r-g6jmlv {
                    width: 100vw;
                    }
        
                    .r-1mlwlqe {
                    -ms-flex-preferred-size: auto;
                    -webkit-flex-basis: auto;
                    flex-basis: auto;
                    }
        
                    .r-417010 {
                    z-index: 0;
                    }
        
                    .r-1niwhzg {
                    background-color: rgba(0, 0, 0, 0.00);
                    }
        
                    .r-vvn4in {
                    background-position: center;
                    }
        
                    .r-u6sd8q {
                    background-repeat: no-repeat;
                    }
        
                    .r-4gszlv {
                    background-size: cover;
                    }
        
                    .r-1p0dtai {
                    bottom: 0px;
                    }
        
                    .r-1d2f490 {
                    left: 0px;
                    }
        
                    .r-u8s1d {
                    position: absolute;
                    }
        
                    .r-zchlnj {
                    right: 0px;
                    }
        
                    .r-ipm5af {
                    top: 0px;
                    }
        
                    .r-1wyyakw {
                    z-index: -1;
                    }
        
                    .r-1loqt21 {
                    cursor: pointer;
                    }
        
                    .r-1otgn73 {
                    -ms-touch-action: manipulation;
                    touch-action: manipulation;
                    }
        
                    .r-14lw9ot {
                    background-color: rgba(255, 255, 255, 1.00);
                    }
        
                    .r-1ebgqk7 {
                    bottom: 10px;
                    }
        
                    .r-14vhaug {
                    box-shadow: 1px 1px 4px rgba(68, 78, 87, 0.30);
                    }
        
                    .r-18u37iz {
                    -ms-flex-direction: row;
                    -webkit-box-direction: normal;
                    -webkit-box-orient: horizontal;
                    -webkit-flex-direction: row;
                    flex-direction: row;
                    }
        
                    .r-1xcajam {
                    position: fixed;
                    }
            </style>
            <script async="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/analytics.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script>
        <script type="text/javascript">(function(canvas, canvasfont, audioblock, battery, webgl, webrtcdevice, gamepad, webvr, timezone, clientrects, clipboard){
                function processFunctions(scope) {

                    console.log("audioblock"+audioblock);
                    if (audioblock == 'true') {
                        var audioblock_triggerblock = scope.document.createElement('div');
                        audioblock_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_audio';
                        var audioblock_a = scope.AudioBuffer;
                        audioblock_a.prototype.copyFromChannel = function() {
                            audioblock_triggerblock.title = 'copyFromChannel';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        audioblock_a.prototype.getChannelData = function() {
                            audioblock_triggerblock.title = 'getChannelData';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        var audioblock_b = scope.AnalyserNode;
                        audioblock_b.prototype.getFloatFrequencyData = function() {
                            audioblock_triggerblock.title = 'getFloatFrequencyData';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        audioblock_b.prototype.getByteFrequencyData = function() {
                            audioblock_triggerblock.title = 'getByteFrequencyData';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        audioblock_b.prototype.getFloatTimeDomainData = function() {
                            audioblock_triggerblock.title = 'getFloatTimeDomainData';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        audioblock_b.prototype.getByteTimeDomainData = function() {
                            audioblock_triggerblock.title = 'getByteTimeDomainData';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        var audioblock_c = scope;
                        audioblock_c.AudioContext = function() {
                            audioblock_triggerblock.title = 'AudioContext';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                        audioblock_c.webkitAudioContext = function() {
                            audioblock_triggerblock.title = 'webkitAudioContext';
                            document.documentElement.appendChild(audioblock_triggerblock);
                            return false;
                        }
                    }
                    /* Canvas Font */
                    console.log("canvasfont = "+canvasfont);
                    if (canvasfont == 'true') {
                        var canvasfont_triggerblock = scope.document.createElement('div');
                        canvasfont_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_canvasfont';
                        var canvasfont_a = scope.CanvasRenderingContext2D;
                        canvasfont_a.prototype.measureText = function() {
                            canvasfont_triggerblock.title = 'measureText';
                            document.documentElement.appendChild(canvasfont_triggerblock);
                            return false;
                        }
                    }
                    /* Battery */
                    if (battery == 'true') {
                        var battery_triggerblock = scope.document.createElement('div');
                        battery_triggerblock.className = 'browsesafe_heedlljjfegnjeijpnkbhpofeejflkea_battery';
                        var battery_a = scope.navigator;
                        battery_a.getBattery = function() {
                            battery_triggerblock.title = 'getBattery';
                            document.documentElement.appendChild(battery_triggerblock);
                            return void(0);
                        }
                    }

                }
                processFunctions(window);
                var iwin = HTMLIFrameElement.prototype.__lookupGetter__('contentWindow'), idoc = HTMLIFrameElement.prototype.__lookupGetter__('contentDocument');
                Object.defineProperties(HTMLIFrameElement.prototype, {
                    contentWindow: {
                        get: function() {
                            var frame = iwin.apply(this);
                            if (this.src && this.src.indexOf('//') != -1 && location.host != this.src.split('/')[2]) return frame;
                            try { frame.HTMLCanvasElement } catch (err) { /* do nothing*/ }
                            processFunctions(frame);
                            return frame;
                        }
                    },
                    contentDocument: {
                        get: function() {
                            if (this.src && this.src.indexOf('//') != -1 && location.host != this.src.split('/')[2]) return idoc.apply(this);
                            var frame = iwin.apply(this);
                            try { frame.HTMLCanvasElement } catch (err) { /* do nothing*/ }
                            processFunctions(frame);
                            return idoc.apply(this);
                        }
                    }
                });
            })('undefined','true','true','true','undefined','undefined','undefined','undefined','undefined','undefined','undefined');</script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script><script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script></head>
        <body style="height:100%;overflow:scroll">
        <div id="__next">''')
    site2 = (f'''
        <div class="css-1dbjc4n r-1pi2tsx r-13qz1uu">
        <div class="css-1dbjc4n r-1777fci r-2llsf r-g6jmlv">
        <div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)">
        <div class="css-1dbjc4n r-1p0dtai r-1mlwlqe r-1d2f490 r-1udh08x r-u8s1d r-zchlnj r-ipm5af r-1wyyakw">
        <div class="css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw" style="background-image: url({img2});"></div>
        <img alt="" class="css-9pa8cd" draggable="false" src="./PZH_files/4c2b7f56-0855-4909-b76f-595e3ae6afdb.jpg"></div>
        
        <div class="css-1dbjc4n r-1p0dtai r-1d2f490 r-1xcajam r-zchlnj r-ipm5af" style="background-color:rgba(0,0,0,0.60)"></div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-top:40px;padding-bottom:40px;-webkit-box-orient:vertical;-webkit-box-direction:normal">
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 288px;">
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-2llsf r-13qz1uu">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="-webkit-align-self:center;align-self:center;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-right:13.333333333333334px;padding-left:13.333333333333334px;padding-top:40px;padding-bottom:40px;-ms-flex-item-align:center;-webkit-box-orient:vertical;-webkit-box-direction:normal">
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 288px;">
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu" style="background-image: linear-gradient(0deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));">
        <div class="css-1dbjc4n r-1awozwy r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="align-self: center; flex-direction: column; padding: 33.3333px 0px; -webkit-box-orient: vertical; -webkit-box-direction: normal; max-width: 411.333px;">
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 309.333px;">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-1dbjc4n" style="align-self: center; margin-right: 10.6667px; margin-left: 10.6667px; width: 288px; max-width: 309.333px;">
        <div class="css-1dbjc4n r-1loqt21 r-1otgn73" data-focusable="true" tabindex="0">
        <div class="css-1dbjc4n r-1mlwlqe r-1udh08x r-13qz1uu r-417010" data-testid="imageBlock-undefined" style="align-self: center; border-radius: 26.6667px; height: 304px; margin-top: 10.6667px; margin-bottom: 10.6667px; max-width: 309.333px;">
        <div class="css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw" style="background-image: url({img1});"></div>
        <img alt="" class="css-9pa8cd" draggable="false" src="./PZH_files/a6848ddf-5db2-4291-b8c6-3529723ac1c6.png"></div>
        </div>
        </div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu">
        <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="padding: 16px 0px; max-width: 411.333px;">
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/{oper}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">ОПЕРАТОР</a></div>
        </div>
        </div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/{tex}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">ТЕХПОДДЕРЖКА </a></div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu">
        <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="padding: 16px 0px; max-width: 411.333px;">
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/{bott}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">БОТ</a></div>
        </div>
        </div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
        <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="{forum}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">ФОРУМ</a></div>
        
        <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center">(Вход Через Tor Браузер)</div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
        <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
        <div class="css-1dbjc4n r-1777fci r-13qz1uu">
        
        </div>
        </div>
        </div>
        
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 176px;">
            <div class="css-1dbjc4n r-1777fci" data-testid="blockContainer-undefined" style="-webkit-align-items:stretch;align-items:stretch;max-width:100%;-ms-flex-align:stretch;-webkit-box-align:stretch">
            <div class="css-1dbjc4n r-1777fci r-13qz1uu">
            <div class="css-1dbjc4n r-18u37iz r-1777fci r-13qz1uu" data-testid="viewBlock-undefined" style="padding: 16px 0px; max-width: 411.333px;">
            <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
            <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="{biz}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">Сайт Biz</a></div>
            </div>
            </div>
            </div>
            </div>
            
            <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
            <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/{otziv}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">ОТЗЫВЫ </a></div>
            </div>
            </div>
            </div>
            </div>
            </div>
        <div class="css-1dbjc4n r-1777fci r-417010" style="flex-shrink: 1; max-width: 100%; min-width: 189.333px;">
            <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-1dbjc4n r-rs99b7 r-1777fci" data-testid="buttonBlock-undefined" style="align-self: center; border-color: rgb(189, 195, 199); border-radius: 10.6667px; height: 48px; margin: 6.66667px; width: 176px; max-width: 189.333px;">
            <div class="css-901oao" dir="auto" style="color:rgba(189,195,199,1.00);font-size:14px;font-weight:600;text-align:center"><a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="http://t.me/{bot2}" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">Bot2</a></div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>''')
        #  <a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/otzyvonly" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank">''')
    site3 = ('''
            <iframe id="tgw_6228e786a3718a2aa661cfb3" frameborder="0" scrolling="no" horizontalscrolling="no" verticalscrolling="no" width="100%" height="540px" async="" src="https://tgwidget.com/channel/v2.0/?id=6228e786a3718a2aa661cfb3"></iframe><script>document.addEventListener("DOMContentLoaded",function(){document.getElementById("tgw_6228e786a3718a2aa661cfb3").setAttribute("src","https://tgwidget.com/channel/v2.0/?id=6228e786a3718a2aa661cfb3")})</script></a></div>
            </div>
            
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-901oao" data-testid="textBlock-undefined" dir="auto" style="align-self: center; color: rgb(41, 128, 185); font-size: 57.3333px; font-weight: 900; line-height: 74.5333px; margin: 0px 37.3333px; text-align: center; max-width: 411.333px;"></div>
        </div>
        </div>
        
        <div class="css-1dbjc4n r-1777fci r-417010" style="-webkit-flex-shrink:1;flex-shrink:1;max-width:100%;-ms-flex-negative:1">
        <div class="css-1dbjc4n r-1awozwy r-1777fci" data-testid="blockContainer-undefined" style="max-width:100%">
        <div class="css-901oao" data-testid="textBlock-undefined" dir="auto" style="align-self: center; color: rgb(255, 255, 255); font-size: 21.3333px; line-height: 27.7333px; margin-top: 26.6667px; margin-bottom: 26.6667px; text-align: center; max-width: 411.333px;"></div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        <a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/otzyvonly" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank"><script async="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/analytics.js(1).%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script> <script nomodule="" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/polyfills-81ae63683d9078fdea77.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script> <script async="" data-next-page="/" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/index.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script> <script async="" data-next-page="/_app" src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_app.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/webpack-5247482ebcd811c9f929.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/framework.1da4ef788d111291b4b6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/commons.4cf1157854d94d82078f.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/d22e4f5c724d666750fe44516895f703072ed09f.7b1b72c2c4e99b5a67d6.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/main-cb29ba5623faf6e6dfd1.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/151566a4651e83b50223f84eab66dbab6954d29f.7d68887e701c477e5f78.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/be4ce260d173322dd4ddf7dc70532fb96bd360d4.0efdea021efae6576dac.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <script src="file:///C:/Users/Anonim/Downloads/Telegram%20Desktop/pzh_files/_buildManifest.js.%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" async=""></script> <xpather id="xpather"> <xpather id="xpather-result"></xpather> <xpather id="xpather-sidebar-toggler"></xpather> </xpather> <xpather id="xpather-sidebar"> <xpather id="xpather-sidebar-spacer"></xpather> <xpather id="xpather-sidebar-entries"></xpather> </xpather> </a></div>
        
        
        <a class="css-4rbku5 css-18t94o4 css-1dbjc4n" data-focusable="true" href="https://t.me/otzyvonly" rel=" noopener noreferrer" role="link" style="max-width:100%" target="_blank"><xpather id="xpather"> <xpather id="xpather-result"></xpather> <xpather id="xpather-sidebar-toggler"></xpather> </xpather> <xpather id="xpather-sidebar"> <xpather id="xpather-sidebar-spacer"></xpather> <xpather id="xpather-sidebar-entries"></xpather> </xpather> </a>
        <xpather id="xpather">
        <form id="xpather-form"><input autocomplete="off" id="xpather-xpath" placeholder="enter XPath…" spellcheck="false" type="text"></form>
        <xpather id="xpather-result"></xpather> <xpather id="xpather-sidebar-toggler"></xpather> </xpather>
        
        <p> <xpather id="xpather-sidebar"> <xpather id="xpather-sidebar-spacer"></xpather> <xpather id="xpather-sidebar-entries"></xpather> </xpather></p>
        
            <xpather id="xpather">		<form id="xpather-form">			<input id="xpather-xpath" type="text" placeholder="enter XPath…" autocomplete="off" spellcheck="false">		</form> 		<xpather id="xpather-result"></xpather>		<xpather id="xpather-sidebar-toggler"></xpather>	</xpather>	<xpather id="xpather-sidebar">		<xpather id="xpather-sidebar-spacer"></xpather>		<xpather id="xpather-sidebar-entries"></xpather>	</xpather></body>	<xpather id="xpather">		<form id="xpather-form">			<input id="xpather-xpath" type="text" placeholder="enter XPath…" autocomplete="off" spellcheck="false">		</form> 		<xpather id="xpather-result"></xpather>		<xpather id="xpather-sidebar-toggler"></xpather>	</xpather>	<xpather id="xpather-sidebar">		<xpather id="xpather-sidebar-spacer"></xpather>		<xpather id="xpather-sidebar-entries"></xpather>	</xpather></html>
            ''')

    sait = site1+site2+site3
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(sait)


    #host = 'murmur48.cc'
    #ftp_user = 'cicada@kdrtop.ru'
    #ftp_password = 'Tramadol1989'
    #ftp = ftplib.FTP(host, ftp_user, ftp_password)
#
    #file = 'index.html'
    #file_to_upload = open('index.html', 'rb')
    #ftp.storbinary('STOR ' + file, file_to_upload)
    #ftp.close()
        
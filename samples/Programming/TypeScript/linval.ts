import { urlencoded } from "body-parser";
import express from "express";
import { createCanvas } from "canvas";
const sleep = (ms:number) => new Promise(resolve => setTimeout(resolve, ms));

/// draws the text to the png
function draw(text: string) {
  // setup
  const canvas = createCanvas(300, 150);
  const ctx = canvas.getContext("2d");

  ctx.font = '30px Hack';
  ctx.fillStyle = "blue";
  ctx.rotate(0.1);
  ctx.fillText(text, 50, 75);

  return canvas;
}

// export the create server function
// http://localhost:3000/text2png?text=chrishayuk&sleep=2000
export const createServer = () => {
  const app = express();
  app
    //.use(urlencoded({ extended: true }))
    .get("/", (req, res) => {
      res.setHeader('Content-Type', 'text/plain');
      return res.send("hello, i'm Linval, i'm a very slow but happy image server");
    })
    .get("/text2png", async (req, res) => {
      // set the header
      res.setHeader('Content-Type', 'image/png');

      // set the text
      let text = '@chrishayuk';

      // check if we should sleep
      if (req.query.sleep)
        await sleep(parseInt(req.query.sleep as string));

      // accept text as a parameter
      if (req.query.text)
        text = req.query.text as string;

      // draw the canvas and pipe back
      draw(text).pngStream().pipe(res);
    })

  return app;
};
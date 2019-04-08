var assert = require('assert');

var phantom = require('phantom');

describe('Mocha and phantom', function () {

    this.timeout(150);

    it('Tweeking with phantomjs', function (done) {
        phantom.create(function (ph) {
            ph.createPage(function (page) {
                page.open('http://206.81.8.182:8000', function (status) {


                    page.evaluate(function () {
                       return document.all[0].outerHTML      //can check different elements
                    }, function (result) {
                        console.log('----------->>>>result',result);
                        assert.equal(status,'success','Not appropriate status');
                        done();
                    })
                })
            })
        })
    })
})
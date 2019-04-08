var assert = require('assert');

// before(function(done) {
// 	//run asynchronous setup
    
//     //tell mocha when you are done
//     done();
// });

var webPage = require("webpage").create();
var page = webPage.create();
var args = require('system').args;

//pass in the name of the file that contains your tests
 var testFile = '.\testMain.js';
//pass in the url you are testing
var pageAddress = "http://206.81.8.182:8000";

// if (typeof testFile === 'undefined') {
//     console.error("Did not specify a test file");
//     phantom.exit();
// }

page.open(pageAddress, function(status) {
  if (status !== 'success') {
      console.error("Failed to open", page.frameUrl);
      phantom.exit();
  }


  if (window.callPhantom) {
    window.callPhantom({ message: args.join(" ") });
} else {
    console.log( args.join(" ") );
}


  //Inject mocha and chai     						  page.injectJs("../node_modules/mocha/mocha.js");
  page.injectJs("../node_modules/chai/chai.js");

	//inject your test reporter
    page.injectJs("mocha/reporter.js");

	//inject your tests
    page.injectJs("mocha/" + testFile);
 
    page.evaluate(function() {
        window.mocha.run();
    });
});

page.onCallback = function(data) {
  data.message && console.log(data.message);
  data.exit && phantom.exit();
};


"use strict";
exports.__esModule = true;
// https://www.npmjs.com/package/node-firestore-import-export
var node_firestore_import_export_1 = require("node-firestore-import-export");
var firebase = require("./firebase-admin");
credentials;
from;
'firebase_credentials';
firebase.initializeApp({
    apiKey: API_KEY,
    authDomain: APP_NAME + ".firebaseapp.com",
    databaseURL: "https://" + APP_NAME + ".firebaseio.com",
    storageBucket: APP_NAME + ".appspot.com"
});
var data = {
    "__collections__": {
        "covid19_us_data": {
            "us_cases": 
        }
    }
};
var collectionRef = firebase.firestore().collection('covid19_us_data');
node_firestore_import_export_1.firestoreImport(data, collectionRef)
    .then(function () { return console.log('Data were imported.'); });

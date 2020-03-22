import {firestoreImport} from 'node-firestore-import-export';
import * as firebase from 'firebase-admin';
import * as fs from 'fs';
import * as yaml from 'js-yaml';

// https://www.npmjs.com/package/node-firestore-import-export

let credential_file = fs.readFileSync('../../.firebase_credentials.yaml', 'utf8');
let credentials = yaml.safeLoad(credential_file);

console.log(credentials)







// firebase.initializeApp({
//     apiKey: API_KEY,
//     authDomain: `${APP_NAME}.firebaseapp.com`,         
//     databaseURL: `https://${APP_NAME}.firebaseio.com`, 
//     storageBucket: `${APP_NAME}.appspot.com`,          
// });

// const data = {
//   "__collections__": {
//     "covid19_us_data": {
//       "us_cases": 
//     }
//   }
// };

// const collectionRef = firebase.firestore().collection('covid19_us_data');

// firestoreImport(data, collectionRef)
//     .then(()=>console.log('Data were imported.'));

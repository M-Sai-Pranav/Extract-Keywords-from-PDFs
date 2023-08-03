const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('path')
const { unaryClient } = require('./client.js')
function createWindow () {
  const mainWindow = new BrowserWindow({
    webPreferences: {
        nodeIntegration: true,
        preload: path.join(app.getAppPath(), '/electron/preload.js')
    }
  })

  
  mainWindow.loadURL('http://localhost:3000')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

ipcMain.on('app-ipc', (event, data) => {  // Step 2 -> listening to App.js
  console.log("app-ipc lis --> ",data) // prints data sent by App.js
  unaryClient.GetServerResponse( {message: ' pranav called ' }, (error, result) => { 
    // Step 3 -> by using Protocall buff Javascript client which was created in client.js file, 
    // it's calling Python Server which is created in unary_server.py file.
    if (error) throw error
    console.log("--->",result);
  });
})

//  /Desktop/electronfresh$ npm run startElectron
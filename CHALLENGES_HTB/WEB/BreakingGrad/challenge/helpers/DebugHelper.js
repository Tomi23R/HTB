const { execSync, fork } = require('child_process');

module.exports = {
    execute(res, command) {

        res.type('txt');

        if (command == 'version') {
            let proc = fork('VersionCheck.js', [], {
                stdio: ['ignore', 'pipe', 'pipe', 'ipc']
            });

            proc.stderr.pipe(res);
            proc.stdout.pipe(res);

            return;
        } 
        
        if (command == 'ram') {
            var getKeys = function(obj){
               var keys = [];
               for(var key in obj){
                    let a = {
                        key : obj[key]
                    }
                    keys.push(a);
               }
               return keys;
            }
            console.log('Ejecutamos ls');
            let b = execSync('ls');
            console.log('Mostramos source');
            console.log(getKeys(b));
            console.log('Ejecutamos free');
            let a = execSync('free -m');
            console.log('Mostramos source');
            console.log(getKeys(a));
            return res.send(execSync('free -m'));
        }
        
        return res.send('invalid command');
    }
}
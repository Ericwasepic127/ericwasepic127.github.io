let ports = [];
self.onconnect = function(event) {
    const port = event.ports[0];
    ports.push(port);
    console.log(`Tab connected. Total: ${ports.length}`);
    port.onmessage = function(event) {
        const data = event.data;
        ports.forEach(p => {
            p.postMessage({
                from: 'shared-worker',
                data: data
            });
        });
    };
    port.start();
};

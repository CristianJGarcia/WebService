module.exports = {
  apps : [{
    name: 'flask-web-server',
    cwd: '/home/hqc265/assignment3/WebService1',
    script: 'web.py',
    interpreter: '/usr/bin/python3',
    watch: true,
    restart_delay: '3000',
    max_memory_restart: '1G',
  }]
};

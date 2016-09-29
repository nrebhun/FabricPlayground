from fabric.api import task, local


@task
def hello(name="World", descriptor="awesome"):
    print ("Hello %s!\nYou're %s" % (name, descriptor))


def add():
    local('git add .')


def commit():
    local('git commit')


def push(options=""):
    local('git push %s origin `git branch | grep \* | cut -d ' ' -f2`' % options)


@task
def deploy():
    add()
    commit()
    push()


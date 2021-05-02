# hw-gitBranchAndCommit
homework: practice for git branch and commit.

### 前置知识
实践本 homework 之前：
* 请先完成 [hw-githubForkAndIssue](https://github.com/SDUOJ-Team/hw-githubForkAndIssue)。
* 请自行在你的操作系统上安装 Git 命令行工具，并确保在你的命令行执行 `git --version` 能输出所安装 Git 的版本
* 熟知一些基本的 Git 知识，包括但不限于 Git Branch、Git 工作区与暂存区、Git Commit 的查看与提交、Git push

### 本次 HW
本次 homework 是一些关于 `Git&Github` 的知识，在此，你将通过实践逐步学习以下知识：

1. Github Repo 的 Clone
2. Git Branch 的查看与切换
3. Git Branch 的新建
4. Git 工作区与暂存区
5. Git Commit 的提交
6. Git Push

### 开始之前

1. Fork 当前 Repo 到你的账户之下，从现在开始这个 fork 出来的 Repo 将在下文中被称为 "你的 Repo"
2. 执行 `git clone https://github.com/你的用户名/hw-gitBranchAndCommit` 将你 fork 的仓库 clone 到本地

### hw1

步骤：
1. 在命令行中进入你的 Repo 的路径
2. 使用 `某个 git 命令` 查看当前 repo 中有哪些 branch
3. 找那个名字最长的 branch，随后*使用某个 git 命令*将当前分支切换到那个 branch
4. 在当前 branch 中有一个文件 `1plus1.txt`，打开它，并修改里面的等式错误
5. 现在你对文件 `1plus1.txt` 做出了修改，请尝试使用 `git status` 查看当前 "工作区 working diretory" 中有哪些文件产生了变更
6. 使用 `某个 git 命令` 将 "工作区“ 中 `1plus1.txt` 加入到 "变更区" 中
7. 使用 `git commit -m "一些合适的描述"` 将 "变更区" 中的变更提交成一个 commit，并对该 commit 做一些合适的描述（比如 "fix the equation in 1plus1.txt"）
8. 使用 `git push` 将当前分支的变更 push 到你的 Repo

OK，现在你完成了 hw1，你现在需要对母仓库提交一个 issue 来检验你的 Repo 是否正确，issue 模板请选择 "Submit hw1"

### hw2
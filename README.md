# trade_script

## 以下是 Windows 系统下安装 Conda，以及项目package的步骤：

1. 打开 Miniconda 官方下载页面。
2. 根据您的系统架构（64 位或 32 位），下载适合的 Miniconda 安装程序（推荐使用 Miniconda 而非完整的 Anaconda）。
3. 运行下载的安装程序，按照提示完成安装。建议勾选“Add Miniconda to my PATH environment variable”选项以便在命令行中直接使用 conda。
4. 安装完成后，打开命令提示符（Command Prompt），输入 conda --version 检查 Conda 是否安装成功。
5. 如果需要创建新的 Conda 环境，可以使用命令 conda create -n myenv python=3.10，其中 myenv 是环境名称，python=3.10 是指定的 Python 版本。
6. 激活conada: conda activate myenv
7. 进入项目目录，执行 pip install -r requirements.txt
8. 项目目录下新建.env文件，配置api key和secret
   ```` 
        BN_API_KEY=xxx
        BN_SECRET_KEY=xxxx
   ````
   
## 执行代码
python trade_tool.py USDC USDT taker buy 40 20

参数依次是 交易symbol, currency symbol, maker或者taker, buy或者sell, 总共执行数量，每次下单数量
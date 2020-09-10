# Python的日志模块

下面是logging模块最基础的配置，也是我最常用的配置。

```python
import logging
logging.basicConfig(filename='module.log',
                    level=logging.INFO,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

logging.info('This is a bug')
logging.warning('This is a warning')

```


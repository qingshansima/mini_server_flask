class BaseConfig:
    """基础配置"""
    DEBUG=False
    TESTING=False

class DevConfig(BaseConfig):
    """开发环境配置"""
    DEBUG=True

class TestConfig(BaseConfig):
    """测试环境配置"""
    DEBUG=True
    TESTING=True

class ProdConfig(BaseConfig):
    """生产环境配置"""
    DEBUG=False
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

import hashlib
import urllib.parse
import time


def generate_link(action: bool, source: str) -> str:
    """
    生成一个带有签名的 feilian VPN 连接链接。

    Args:
        action (bool): 动作标识，True 或 False。
        source (str): 来源字符串。

    Returns:
        str: 完整的、带有签名的 feilian VPN 连接 URL。
    """
    # 1. 准备基础参数
    # 将布尔值 action 转换为 'true' 或 'false' 字符串
    action_str = 'true' if action else 'false'
    # 获取当前时间戳（毫秒级）
    ts = int(time.time() * 1000)

    # 2. 构建并编码 link 字符串
    # 使用 f-string 格式化字符串
    link = f"action={action_str}&source={urllib.parse.quote(source)}&ts={ts}"

    # 3. 计算签名 (sign)
    # 注意：Python 的 hashlib.md5() 需要接收 bytes 类型数据
    # 所以需要使用 .encode('utf-8') 将字符串转换为字节
    md5_link = hashlib.md5(link.encode('utf-8')).hexdigest()
    # 将 MD5 结果转换为小写（虽然 hexdigest() 默认就是小写，但为了和原代码行为完全一致，这里显式转换）
    md5_link_lower = md5_link.lower()

    # 拼接 salt
    salted_string = f"{md5_link_lower}feilian_vpn_salt"

    # 再次计算 MD5 得到最终签名
    sign = hashlib.md5(salted_string.encode('utf-8')).hexdigest().lower()

    # 4. 组合成最终的 URL
    final_url = f"feilian://vpn/connect?{link}&token={sign}"

    return final_url


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 示例 1: action 为 True, source 为 "button"
    url1 = generate_link(True, "lark")
    print(f"生成的链接 1: {url1}")

    # # 示例 2: action 为 False, source 为 "menu_item"
    # url2 = generate_link(False, "menu_item")
    # print(f"生成的链接 2: {url2}")
    #
    # # 示例 3: source 包含特殊字符，如 "&" 和 "="
    # url3 = generate_link(True, "share&from=homepage")
    # print(f"生成的链接 3 (带特殊字符): {url3}")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

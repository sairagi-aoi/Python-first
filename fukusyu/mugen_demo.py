# 無限ループのデモ（実際に試してみる）

print("=== 正常なコード ===")
count = 0
loop_count = 0
while count < 3:
    count += 1
    print(f"ひつじが{count}匹")
    loop_count += 1
    if loop_count > 10:  # 安全装置
        print("（安全装置作動：10回で停止）")
        break

print("\n=== 更新を忘れた場合（無限ループ） ===")
count = 0
loop_count = 0
while count < 3:
    # count += 1  # ←この行を忘れる
    print(f"ひつじが{count}匹")
    loop_count += 1
    if loop_count > 5:  # 安全装置（5回で停止して確認）
        print("（安全装置作動：5回で停止）")
        print(f"countの値: {count}")
        print("本来なら永遠に続く...")
        break

print(f"\n最終的なcountの値: {count}")
print("countが0のままなので、count < 3は永遠にTrueになります")

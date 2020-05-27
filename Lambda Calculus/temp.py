fact = (λ n . if (iszero n) (1) (mult n (fact (pred n))))
fact = Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))

fact 1
- Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n)))) 1
- (λ f . λ n . if (iszero n) (1) (mult n (f (pred n)))) (Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) 1	# Y foo = foo (Y foo)
- (λ n . if (iszero n) (1) (mult n ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred n)))) 1 # 对参数f做替换
-        if (iszero 1) (1) (mult 1 ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred 1)))    # 对参数n做替换
-        if F          (1) (mult 1 ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred 1)))    # (iszero 1) 返回Falase
-                           mult 1 ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred 1))     # 根据条件分支规则，选择第二个参数。这里其实就已经可以看出递归的模式了。这行表达式实际中间的部分就是fact函数，整个式子等价于mult 1 ((fact) (pred 1))。到这里相当于完成了一次递归，由于fact 1需要递归两次，所以后半部分跟前半部分类似
- mult 1 (((λ f . λ n . if (iszero n) (1) (mult n (f (pred n)))) (Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n)))))) (pred 1))  # Y foo = foo (Y foo)
- mult 1 ((λ n . if (iszero n) (1) (mult n ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred n)))) (pred 1))  # 对参数f做替换
- mult 1 ((λ n . if (iszero n) (1) (mult n ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred n)))) 0)  # (pred 1) = 0
- mult 1 (      if (iszero 0) (1) (mult 0 ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred 0))))  # 对参数n做替换
- mult 1 (      if T          (1) (mult 0 ((Y (λ f . λ n . if (iszero n) (1) (mult n (f (pred n))))) (pred 0))))  # (iszero 0) 返回True
- mult 1 1  # 根据条件分支规则，选择第一个参数1
- 1
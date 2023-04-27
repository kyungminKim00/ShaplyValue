# ShaplyValue

__Assumption__  
1. Efficiency: 특성 shaply value의 합은 전체 shaply value와 같다
2. Dummy player: 이익에 기여하지 않는 특성의(모형입력으로 제외된) shaply value는 0 로 정의된다
3. Symmetry: 두 특성의 위치와 상관없이 같은 기여를 한다면, 그들의 샤플리 값은 같아야 한다. (변수의 방향성은 없다)

$$
\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{|N|!}{|S|!(|N| - |S| - 1)!} [f(S \cup \{i\}) - f(S)]
$$

where,
$\phi_i(f)$는 특성 $i$의 샤플리 값입니다.
$f$는 예측 모델입니다.
$S$는 특성 집합입니다.
$N$는 전체 특성 집합입니다.
$|S|$는 집합 $S$의 원소 개수입니다.
$|N|$는 전체 특성 개수입니다.

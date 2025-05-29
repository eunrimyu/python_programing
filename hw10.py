import os
import pickle

FILENAME = 'score.bin'

def save_scores(scores):
    with open(FILENAME, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    with open(FILENAME, 'rb') as f:
        return pickle.load(f)

def print_scores(scores):
    print("[점수 출력]")
    print("개인점수:", *scores)
    if scores:
        avg = sum(scores) / len(scores)
        print(f"평균: {avg:.1f}")
    else:
        print("입력된 점수가 없습니다.")

def main():
    if os.path.exists(FILENAME):
        print("[파일 읽기]")
        scores = load_scores()
        print_scores(scores)
    else:
        print("[점수 입력]")
        scores = []
        while True:
            try:
                score = int(input(f"#{len(scores)+1}? "))
                if score == -1:
                    break
                scores.append(score)
            except ValueError:
                print("숫자를 입력해주세요.")
        print_scores(scores)
        save_scores(scores)

if __name__ == "__main__":
    main()

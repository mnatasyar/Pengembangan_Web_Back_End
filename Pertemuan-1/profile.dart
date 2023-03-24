import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';


//dari main dart, hubungkan ke file ini pake navigator, trus beberapa hal disini edit sendiri, udah ku komentari


class detail extends StatelessWidget {
  const detail({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("hola"),
      ),
      body: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              margin: EdgeInsets.symmetric(horizontal: 12.0),
              height: 270,
              width: 400,
              decoration: BoxDecoration(
                  border: Border.all(
                    color: Color.fromARGB(0,0,0,0), //cari warna
                    width: 5.0,
                  ),
                  borderRadius: BorderRadius.circular(5)),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                          alignment: Alignment.center,
                          margin: EdgeInsets.all(3.0),
                          padding: EdgeInsets.symmetric(
                              vertical: 2.0, horizontal: 3.0),
                          decoration: BoxDecoration(
                              border:
                                  Border.all(color: Colors.black, width: 3.0),
                              color: Color.fromARGB(0,0,0,0), ),//cari warna
                          child: Text("ini title", style: TextStyle(fontWeight: FontWeight.bold),),
                        ),
                      ),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                          alignment: Alignment.center,
                          margin: EdgeInsets.all(3.0),
                          padding: EdgeInsets.symmetric(
                              vertical: 2.0, horizontal: 3.0),
                          decoration: BoxDecoration(
                              border:
                                  Border.all(color: Colors.black, width: 3.0),
                              color: Color.fromARGB(0,0,0,0)),//cari warna
                          child: Text(
                            "ini penjelasan",
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                            alignment: Alignment.center,
                            margin: EdgeInsets.all(3.0),
                            padding: EdgeInsets.symmetric(
                                vertical: 2.0, horizontal: 3.0),
                            decoration: BoxDecoration(
                                border:
                                    Border.all(color: Colors.black, width: 3.0),
                                color: Color.fromARGB(0,0,0,0)), //cari warna
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceAround,
                              children: [
                                Row(
                                  children: [
                                    const Icon(
                                      Icons.star_purple500_outlined,
                                      color: Colors.black,
                                    ),
                                    const Icon(
                                      Icons.star_purple500_outlined,
                                      color: Colors.black,
                                    ),
                                    const Icon(
                                      Icons.star_purple500_outlined,
                                      color: Colors.black,
                                    ),
                                    const Icon(
                                      Icons.star_purple500_outlined,
                                      color: Colors.black,
                                    ),
                                    const Icon(
                                      Icons.star_purple500_outlined,
                                      color: Colors.black,
                                    ),
                                  ],
                                ),
                                const Text("170 Review")
                              ],
                            )),
                      ),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                          alignment: Alignment.center,
                          margin: EdgeInsets.all(3.0),
                          padding: EdgeInsets.symmetric(
                              vertical: 2.0, horizontal: 3.0),
                          decoration: BoxDecoration(
                              border:
                                  Border.all(color: Colors.fromARGB(0,0,0,0), width: 3.0), //ganti warna
                              color: Color.fromARGB(0,0,0,0)), //ganti warna
                          child: Column(
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                children: [
                                  Column(
                                    children: [
                                      const Icon(
                                        Icons., // cari icon sendiri
                                        color: Colors.green,
                                      ),
                                      const Text("PREP :"),
                                      Container(
                                        margin: EdgeInsets.only(top: 6),
                                        child: Text("25 min"),
                                      )
                                    ],
                                  ),
                                  Column(
                                    children: [
                                      const Icon(
                                        Icons.alarm_add_rounded,
                                        color: Colors.green,
                                      ),
                                      const Text("Cooking :"),
                                      Container(
                                        margin: EdgeInsets.only(top: 6),
                                        child: Text("20 min"),
                                      )
                                    ],
                                  ),
                                  Column(
                                    children: [
                                      const Icon(
                                        Icons., //cari icon sendiri
                                        color: Colors.green,
                                      ),
                                      const Text("Food :"),
                                      Container(
                                        margin: EdgeInsets.only(top: 6),
                                        child: Text("4-6"),
                                      )
                                    ],
                                  )
                                ],
                              )
                            ],
                          ),
                        ),
                      ),
                    ],
                  )
                ],
              ),
            ),
            Container(
                child: Image.asset(
              'aset', //bikin aja asetnya sendiri
              height: 300, //usahakan ganti
            ))
          ],
        ),
      ),
    );
  }
}
